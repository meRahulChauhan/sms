import re
from django.contrib.auth.hashers import make_password,check_password
from django.core.serializers import serialize
from django.shortcuts import render ,redirect
from django.urls import reverse 
from django.template import loader
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
#import student list from student model
from student.models import Student
from usertable.models import usertable
#from django.contrib.auth import authenticate,login
from request.models import QueryRequest
from teacher.models import teacher
from django.contrib.auth.models import User
# Create your views here.
#multiple string based name with multiple spaces
expression_full=r"^[a-zA-Z]+(\s[a-zA-Z]+)*\s[a-zA-Z]+$"
#single name with no space
expression_single=r"^[a-zA-Z]+$"
#single number 
expression_number=r"^[0-9]+$"
#function for matching expression that return t/f based on condition

def match_expression(expression,string_data):
    string_data= re.sub(r'\s+', ' ', string_data).strip()
    return bool(re.match(expression,string_data))
#check if email exist into the database 
def check_email(request,email):
    #check if email already exist in usertable
    u=usertable.objects.filter(email=email).exists()
    #check if email already exist in teachertable
    t=teacher.objects.filter(email=email).exists()
    #check if email already exist in admin-user-table
    a=User.objects.filter(email=email).exists()
    return  u or t or a
def not_exist(request,email):
    #check if email already exist in usertable
    u=usertable.objects.filter(email=email).exists()
    #check if email already exist in teachertable
    t=teacher.objects.filter(email=email).exists()
    #check if email already exist in admin-user-table
    a=User.objects.filter(email=email).exists()
    return  not (u or t or a)
#function for contact page query/contact 
def user_query(request):
    if request.method == 'POST':
        email = request.POST.get("email").lower()

        if request.POST.get("name") == "":
            return JsonResponse({'name_error': True})
        else:
            name = request.POST.get("name")
            if match_expression(expression_single,name) or match_expression(expression_full,name):
                name = re.sub(r'\s+', ' ', name).strip()
            else:
                return JsonResponse({'name_error': True})

        if request.POST.get("msg_body") == "":
            return render(request, 'home/index.html', {'msg_body': True})
        else:
            if len(request.POST.get("msg_body")) < 15:
                return JsonResponse({'shortmsg':'minimum 15 character required'})
            else:
                msg_body = request.POST.get("msg_body")
        
        try:
            queryobj = QueryRequest(name=name, email=email, body=msg_body)
            queryobj.save()
            response_query={
                'success':'successfully query submitted',
                'user':{
                    'name':queryobj.name,
                    'email':queryobj.email
                }
            }
            return JsonResponse(response_query)
        except Exception as e:
            print('error occured ',e)
            return JsonResponse({'error ':str(e)})
    return render(request, 'home/index.html')

def stateless(request):
	return HttpResponse("hello! Django is working well")

def thanks(request):
	return HttpResponse("<h1>I am redirected from form.html</h1>")

def user_registration(request):
    if request.method == 'POST':
        # get email
        email = request.POST.get("email").lower()
        if check_email(request,email):
            return JsonResponse({'email_error':True})
        # get name
        elif  request.POST.get('name') == "":
            return JsonResponse({'name_error': True})
        else:
            name = request.POST.get('name')
            print(name)
            if match_expression(expression_single, name) or match_expression(expression_full, name):
                name = re.sub(r'\s+', ' ', name).strip()
            else:
                return JsonResponse({'name_error': True})    
        
        # get and verify passwords
        pw0 = request.POST.get('password0')
        pw1 = request.POST.get('password1')
        print('Name: ', name, ', Email: ', email, ', Password1: ', pw0, ', Password1: ', pw1)       
        if pw0 == pw1:
            print('password match')
        else:   
            print('password not matched')
            return JsonResponse({'password_error': True})
        try:

            usertable_obj = usertable(name=name, email=email, password=make_password(pw0))
            usertable_obj.save()
            print("user with email", email, " saved to database")
            response_data = {
                'message': 'User successfully registered',
                'user': {
                    'name': usertable_obj.name,
                    'email': usertable_obj.email
                }
            }
            return JsonResponse(response_data)
        
        except Exception as e:
            print('error occured ', e)
            return JsonResponse({'error': str(e)})
          
    return render(request, 'home/user_registration.html')

def user_add(request):
    if request.method == 'POST':
        # get email
        email = request.POST.get("email").lower()
        if check_email(request,email):
            return JsonResponse({'email_error':True})
        # get name
        elif  request.POST.get('name') == "":
            return JsonResponse({'name_error': True})
        else:
            name = request.POST.get('name')
            print(name)
            if match_expression(expression_single, name) or match_expression(expression_full, name):
                name = re.sub(r'\s+', ' ', name).strip()
            else:
                return JsonResponse({'name_error': True})    
        
        # get and verify passwords
        pw0 = request.POST.get('password0')
        pw1 = request.POST.get('password1')
        print('Name: ', name, ', Email: ', email, ', Password1: ', pw0, ', Password1: ', pw1)       
        if pw0 == pw1:
            print('password match')
        else:   
            print('password not matched')
            return JsonResponse({'password_error': True})
        try:

            usertable_obj = usertable(name=name, email=email, password=make_password(pw0))
            usertable_obj.save()
            print("user with email", email, " saved to database")
            response_data = {
                'message': 'User successfully registered',
                'user': {
                    'name': usertable_obj.name,
                    'email': usertable_obj.email
                }
            }
            return JsonResponse(response_data)
        
        except Exception as e:
            print('error occured ', e)
            return JsonResponse({'error': str(e)})
          
    return render(request, 'usertable/user_add.html')

def user_update(request,pk):
    usr=usertable.objects.get(pk=pk)
    if request.method == 'POST':
        email = request.POST.get("email").lower().strip()
        name=request.POST.get('name')
        if name is not None:
            name = request.POST.get('name')
            print(name)
            if match_expression(expression_single, name) or match_expression(expression_full, name):
                name = re.sub(r'\s+', ' ', name).strip().title()
            else:
                return JsonResponse({'name_error': True})    
        
        # get and verify passwords
        pw0 = request.POST.get('password0')
        pw1 = request.POST.get('password1')
        print('Name: ', name, ', Email: ', email, ', Password1: ', pw0, ', Password1: ', pw1)       
        if pw0 == pw1:
            print('password match')
        else:   
            print('password not matched')
            return JsonResponse({'password_error': True})
        try:
            #usr=usertable.objects.get(pk=pk)
            exist_usr=usertable.objects.filter(email=email).exclude(pk=pk).first()
            if exist_usr:
                return JsonResponse({'Email Already Exists':True})
            else:
                usr.name = name
                usr.email=email
                usr.save()
                print("user with email", email, " saved to database")
                response_data = {
                'message': 'User successfully registered',
                'user': {
                    'name': usr.name,
                    'email': usr.email
                        }
                    }
            return JsonResponse(response_data)
        
        except Exception as e:
            print('error occured ', e)
            return JsonResponse({'error': str(e)})
          
    return render(request, 'usertable/user_update.html',{'usr':usr})


def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if request.POST.get('password')=='':
            return JsonResponse({'password_error':True})
        else:
            password=request.POST.get('password')
            print("Email: ",email," Password: ",password,"not  hashed password: ",password)
            try:
                usr=usertable.objects.filter(email=email).first()
                t=teacher.objects.filter(email=email).first()
                adm=User.objects.filter(email=email).first()
                if usr:
                    if check_password(password,usr.password):
                        print("user logged in successfully ")
                        request.session['email']=usr.email
                        return JsonResponse({'login':True})
                    else:
                        print('invalid password')
                        return JsonResponse({'password_error':True})
                elif t :
                    if check_password(password,t.password):
                        print("user logged in successfully ")
                        request.session['email']=t.email
                        return JsonResponse({'login':True})
                    else:
                        print('invalid password')
                        return JsonResponse({'password_error':True})
                elif adm:
                    if check_password(password,adm.password):
                        print("user logged in successfully ")
                        request.session['email']=adm.email
                        data={
                            'login':True,
                            'redirect_url': reverse('student:student_list')

                        }
                        return JsonResponse(data)                  
                    
                    else:
                        print('invalid password')
                        return JsonResponse({'password_error':True})
                else:
                    return JsonResponse({'email_error':True})    

            except Exception as e :
                print('Exception ',e)        
                return JsonResponse({'error':str(e)})
    return render(request,'home/login.html')
#dashboard views