from django.shortcuts import render,redirect
from django.http import JsonResponse
import re
from .models import EducationalBoard,EducationalYear,Exam
# Create your views here.
#multiple string based name with multiple spaces
expression_full=r"^[a-zA-Z]+(\s[a-zA-Z]+)*\s[a-zA-Z]+$"
date_range = r'\b\d{4}-\d{4}\b'
#single name with no space
expression_single=r"^[a-zA-Z]+$"
#single number 
expression_number=r"^[0-9]+$"
#function for matching expression that return t/f based on condition

def match_expression(expression,string_data):
    string_data= re.sub(r'\s+', ' ', string_data).strip()
    return bool(re.match(expression,string_data))

def Education_board_view(request):
    education_board=EducationalBoard.objects.all()
    return render(request,'board/education_board_view.html',{'board_list':education_board})

def Education_board_add(request):
    education_board=EducationalBoard.objects.all()
    if request.method=='POST':
        if request.POST.get('name')=="":
            return JsonResponse({'name_error':True})
        else:
            name=request.POST.get('name')
            if match_expression(expression_full,name) or match_expression(expression_single,name):
                name=name.title()
            else:
                return JsonResponse({'name_error':True})
            try:
                education_board_obj=EducationalBoard.objects.create(name=name)
                education_board_obj.save()
                return JsonResponse({'successfully boardname added':True})
            except Exception as e:
                return JsonResponse({'Exception Occured':str(e)})
    
    return render(request,'board/education_board_add.html',{'board':education_board})

def Education_board_delete(request,pk):
    education_board=EducationalBoard.objects.get(pk=pk)
    if request.method=='POST':
        education_board.delete()
        return redirect('admins:board_list')
    return render(request,'board/education_board_delete.html',{'education_board':education_board})

def Education_board_update(request,pk):
    education_board=EducationalBoard.objects.get(pk=pk)
    if request.method=='POST':
        if request.POST.get('name')=="":
            return JsonResponse({'name_error':True})
        else:
            name=request.POST.get('name')
            if match_expression(expression_full,name) or match_expression(expression_single):
                name=name.title()
            else:
                return JsonResponse({'name_error':True})
            try:
                education_board.name=name
                education_board.save()
                return JsonResponse({'successfully boardname added':True})
            except Exception as e:
                return JsonResponse({'Exception Occured':str(e)})
    
    return render(request,'board/education_board_update.html',{'board_name':education_board})

def Education_year_view(request):
    year_view=EducationalYear.objects.all()
    return render(request,'board/educational_year_view.html',{'year_view':year_view})

def Education_year_add(request):
    year_list = EducationalYear.objects.all()
    if request.method == 'POST':
        year = request.POST.get('name')
        print("Year received:", year)  # Debugging line
        if not year:
            return JsonResponse({'year_error': True})
        
        if match_expression(date_range, year):
            try:
                new_year = EducationalYear.objects.create(year=year)
                new_year.save()
                return JsonResponse({'successfully year added': True})
            except Exception as e:
                return JsonResponse({'Exception Occured': str(e)})
        else:
            return JsonResponse({'Use this format 2020-2021': True})
    
    return render(request, 'board/education_board_add.html', {'year_list': year_list})

        


def Education_year_update(request,pk):
    y=EducationalYear.objects.get(pk=pk)
    if request.method == 'POST':
        year = request.POST.get('name')
        print("Year received:", year)  # Debugging line
        if not year:
            return JsonResponse({'year_error': True})
        
        if match_expression(date_range, year):
            try:
                y.year=year
                y.save()
                return JsonResponse({'successfully year Updated': True})
            except Exception as e:
                return JsonResponse({'Exception Occured': str(e)})
        else:
            return JsonResponse({'Use this format 2020-2021': True})   
    return render(request,'board/educational_year_update.html',{'y':y})     

def Education_year_delete(request,pk):
    year=EducationalYear.objects.get(pk=pk)
    if request.method=='POST':
        year.delete()
        return redirect('admins:year_view')

    return render(request,'board/educational_year_view.html',{'year':year})    

def Exam_view(request):
    exam=Exam.objects.all()
    return render(request,'board/exam_list.html',{'exam':exam})

def Exam_add(request):
    exam=Exam.objects.all()
    if request.method=='POST':
        name=request.POST.get('name')
        exam_type=request.POST.get('exam_type')
        if name is  None:
            return JsonResponse({'exam_name_error':True})
        else:
            if match_expression(expression_single,name) or match_expression(expression_full,name):
                name=name.title()
                try:
                    ex=Exam.objects.create(name=name,exam_type=exam_type)
                    ex.save()
                    return JsonResponse({'success':True})
                except Exception as e:
                    return JsonResponse({'error:':str(e)})    
            else:                
                return JsonResponse({'exam_name_error':True})
    return render(request,'board/exam_add.html',{'exam':exam})

def Exam_update(request,pk):
    exam=Exam.objects.get(pk=pk)
    if request.method=='POST':
        exam_type=request.POST.get('exam_type')
        name=request.POST.get('name')
        if name is None:
            return JsonResponse({'exam_name_error':True})
        else:
            if match_expression(expression_single,name) or match_expression(expression_full,name):
                name=name.title()
                try:
                    exam.name=name
                    exam.exam_type=exam_type
                    exam.save()
                    return JsonResponse({'updated_successfully':True})
                except Exception as e:
                    return JsonResponse({'exception':str(e)})    
            else:
                return JsonResponse({'exam_name_error':True})    

    return render(request,'board/exam_update.html',{'exam':exam})

def Exam_delete(request,pk):
    exam=Exam.objects.get(pk=pk)
    if request.method=='POST':
        exam.delete()
        return redirect('admins:exam_view')
    return render(request,'board/exam_delete.html',{'exam':exam})
