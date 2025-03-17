from django.shortcuts import render,redirect
from django.core.serializers import serialize
from django.utils.timezone import now
from .models import Student, StudentInfo, ParentInfo, Attendence, Subject, Fee
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist
import json
from django.urls import reverse
import re
from .forms import StudentForm
from admin_.models import EducationalBoard,EducationalYear        
from home.models import Choice


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
#Create your views here.

def student_list_view(request):
    students=Student.objects.all()    
    student_count=len(students)
    paginator=Paginator(students,20)
    pgn=request.GET.get('page')
    page_object=paginator.get_page(pgn)
    return render(request,'student/student_list_view.html',{'page_obj':page_object,'st_count':student_count})
def student_view_by_class(request,pk):
    students=Student.objects.filter(student_class=pk)  
    student_count=len(students) 
    paginator=Paginator(students,20)
    pgn=request.GET.get('page')
    page_object=paginator.get_page(pgn)
    return render(request,'student/student_list_view.html',{'page_obj':page_object,'st_count':student_count})

def add_student(request):
    student_class = Choice.class_choice
    education_board = EducationalBoard.objects.all()
    educational_year = EducationalYear.objects.all()

    if request.method == 'POST':
        board_name = request.POST.get('board_name')
        class_name = request.POST.get('class_name')
        email = request.POST.get('email')

        if Student.objects.filter(email=email).exists():
            return JsonResponse({'email_exist': True})

        if request.POST.get('name') == "":
            return JsonResponse({'name_error': True})
        else:
            name = request.POST.get('name')
            print(f"rawname {name}")
            if name is not None:
                # Validate and process the name
                if match_expression(expression_single, name) or match_expression(expression_full, name):
                    name = re.sub(r'\s+', ' ', name).strip().title()
                else:
                    return JsonResponse({'name_error': True})
        print(f"name {name}, email {email}, class_name {class_name},type {type(class_name)} board {board_name} ")

        try:
            educational_board_obj = EducationalBoard.objects.get(pk=board_name)

            new_student = Student.objects.create(
                educational_Board_id=educational_board_obj,
                year=EducationalYear.objects.first(),  # Adjust this to select the correct year
                name=name,
                student_class=class_name,
                email=email,
                status='PB'  # 'PB' is a placeholder for Published student
            )
            new_student.save()
            new_student_id=new_student.student_id
            print(new_student_id)
            return redirect('student:save_subject',pk=new_student_id)
        except ObjectDoesNotExist:
            return JsonResponse({'exception error': 'Educational Board does not exist.'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, safe=False)

    context = {
        'education_board': education_board,
        'student_class': student_class,
        'educational_year': educational_year
    }
    return render(request, 'student/student_form.html', context)

def save_subject(request, pk):
    student = Student.objects.get(pk=pk)
    s = Choice.subject_list

    # Create a copy of 'base', 'optional', and 'elective' to avoid mutation of the original lists
    sub_base = s[student.student_class]['base'].copy()
    sub_optional = s[student.student_class]['optional'].copy()
    sub_elective = s[student.student_class]['elective'].copy()

    print(f'Sample base: {sub_base}')
    print(f'Sample optional: {sub_optional}')
    print(f'Sample elective: {sub_elective}')

    if request.method == 'POST':
        # Append optional and elective subjects if provided in the POST request
        if request.POST.get('optional') is not None:
            sub_base.append(request.POST.get('optional'))
        if request.POST.get('elective') is not None:
            sub_base.append(request.POST.get('elective'))

        # Check and create Subject instances if they don't exist
        if Subject.objects.filter(pk=pk) is not None:
            try:
                print(f'Final total: {sub_base}')
                for data in sub_base:
                    if not Subject.objects.filter(student_id=student, subject=data).exists():
                        Subject.objects.create(student_id=student, subject=data)

                # Reset sub_base to avoid issues with subsequent requests
                sub_base = s[student.student_class]['base'].copy()
                if not StudentInfo.objects.filter(student_id=pk):
                    return redirect('student:studentInfo',pk=student.pk)
                return redirect('student:student_profile', pk=student.pk)
            except Exception as e:
                return JsonResponse({'exception': str(e)})
        else:
            return redirect('student:profile')

    return render(request, 'student/choose_subject.html', {
        'sub_base': sub_base,
        'sub_elective': sub_elective,
        'sub_optional': sub_optional,
    })

def student_update(request,pk):
    student_class = Choice.class_choice
    education_board = EducationalBoard.objects.all()
    educational_year = EducationalYear.objects.all()
    student=Student.objects.get(pk=pk)
    if request.method == 'POST':
        board_name = request.POST.get('board_name')
        class_name = request.POST.get('class_name')
        email = request.POST.get('email')

        if request.POST.get('name') == "":
            return JsonResponse({'name_error': True})
        else:
            name = request.POST.get('name')
            print(f"rawname {name}")
            if name is not None:
                # Validate and process the name
                if match_expression(expression_single, name) or match_expression(expression_full, name):
                    name = re.sub(r'\s+', ' ', name).strip().title()
                else:
                    return JsonResponse({'name_error': True})
        print(f"name {name}, email {email}, class_name {class_name}, board {board_name}")

        try:
            educational_board_obj = EducationalBoard.objects.get(pk=board_name)
            existing_student=Student.objects.filter(email=email).exclude(pk=pk).first()
            if existing_student:
                return JsonResponse({'email_exist':True})
            else:                
                print(f"{educational_board_obj},{board_name},{name},{email},{class_name}")
                student.educational_Board_id=educational_board_obj
                student.year=EducationalYear.objects.first()  # Adjust this to select the correct year
                student.name=name
                student.student_class=class_name
                student.email=email
                student.status='PB'  # Assuming 'PB' is a placeholder, you should use the actual value
                student.save()
                return JsonResponse({'success': True})
        except ObjectDoesNotExist:
            return JsonResponse({'except_error': 'Educational Board does not exist.'})
        except Exception as e:
            return JsonResponse({'except_error': str(e)}, safe=False)    
    context = {
        'student':student,
        'education_board': education_board,
        'student_class': student_class,
        'educational_year': educational_year
    }
    return render(request,'student/student_updation_form.html',context)    

def student_delete(request,pk):
    student=Student.objects.get(pk=pk)
    if request.method=='POST':
        student.delete()
        return redirect('student:student_list')
    return render(request, 'student/student_delete_confirmation.html', {'student': student})
                                                     
def student_info_view(request):
    student_info=StudentInfo.objects.all()
    student_info_json=serialize('json',student_info)
    return render(request,'student/student_info_view.html',{'studen_info_json':student_info_json})

def parent_info_view(request):    
    parents_info=ParentInfo.objects.all()
    parent_info_json=serialize('json',parents_info)
    return render(request,'home/parent_info_view.html',{'parent_info_json':parent_info_json})

def attendence_view(request):
    attendence=Attendence.objects.all()
    attendence_json=serialize('json',attendence)
    return render(request,'home/attendence_view.html',{'attendence_json':attendence_json})

def subject_view(request):    
    subject=Subject.objects.all()
    subject_json=serialize('json',subject)
    return render(request,'home/subject_view.html',{'subject_json':subject_json})
def fee(request):    
    fee=Fee.objects.all()
    fee_json=serialize('json',fee)
    return render(request,'home/dashboard.html',{'fee_json':fee_json})

def studentInfo(request, pk):
    student = Student.objects.get(student_id=pk)
    
    gender = dob = gaurdian = address = city = district = postal = state = country = None

    if request.method == 'POST':
        gender = request.POST.get('gender')
        if not gender:
            return JsonResponse({'gender_error': 'Invalid gender selected'})

        dob = request.POST.get('dob')
        if not dob:
            return JsonResponse({'dob_error': 'Date of birth is required'})

        gaurdian = request.POST.get('gaurdian').title()
        if gaurdian and not (
            match_expression(expression_full, gaurdian) or match_expression(expression_single, gaurdian)
        ):
            return JsonResponse({'gaurdian_error': 'Invalid gaurdian name'})
        mother_name=request.POST.get('mother').title()
        father_name=request.POST.get('father').title()
        if not (match_expression(expression_single, father_name) or match_expression(expression_full, father_name)):
            return JsonResponse({'father_name_error':True})
        
        email=request.POST.get('email').lower()

        phone=request.POST.get('phone')
        if not (match_expression(expression_number, phone) and len(phone)==10):
            return JsonResponse({'phone_error':True})
        
        address = request.POST.get('address').title()
        if not address:
            return JsonResponse({'address_error': 'Invalid address'})

        city = request.POST.get('city').title()
        if not match_expression(expression_single, city):
            return JsonResponse({'city_error': 'Invalid city name'})

        district = request.POST.get('district').title()
        if not match_expression(expression_single, district) or match_expression(expression_full, city):
            return JsonResponse({'district_error': 'Invalid district name'})

        postal = request.POST.get('postal')
        if not (postal and match_expression(expression_number, postal) and len(postal) == 6):
            return JsonResponse({'postal_error': 'Invalid postal code, must be 6 digits'})

        state = request.POST.get('state').title()
        if not match_expression(expression_single, state) or  match_expression(expression_full, state):
            return JsonResponse({'state_error': 'Invalid state name'})

        country = request.POST.get('country').title()
        if not match_expression(expression_single, country) or match_expression(expression_full, country):
            return JsonResponse({'country_error': 'Invalid country name'})

        print(f"Gender: {gender}, DOB: {dob}, gaurdian: {gaurdian}, Address: {address}, "
              f"City: {city}, District: {district}, Postal: {postal}, State: {state}, Country: {country}")

        try:
            if not StudentInfo.objects.filter(student_id=pk).exists():
                StudentInfo.objects.create(
                student_id=student,
                gender=gender,
                dob=dob,
                gaurdian=gaurdian,
                address=address,
                city=city,
                district=district,
                postal_code=postal,
                state=state,
                country=country
            )
            if not ParentInfo.objects.filter(student_id=pk).exists():
                ParentInfo.objects.create(
                student_id=student,
                mother_name=mother_name,
                father_name=father_name,
                parent_phone=phone,
                email=email,
                address=address,
                postal_code=postal,
                city=city,
                district=district,
                country=country,
            )
            return redirect('student:student_profile',pk=pk )
        except Exception as e:
            # Handle potential database errors
            return JsonResponse({'exception': str(e)})

    # Pass gender choices to the template
    context = {
        'gender': Choice.gender_choice,
    }
    return render(request, 'student/student_info_form.html', context)

def student_profile(request, pk):
    student = Student.objects.get(pk=pk)
    subjects = Subject.objects.filter(student_id=pk)
    
    try:
        student_info = StudentInfo.objects.get(student_id=student)
        has_info = True
    except StudentInfo.DoesNotExist:
        student_info = None
        has_info = False

    try:
        parent=ParentInfo.objects.get(student_id=pk)
        parent_info=True
    except ParentInfo.DoesNotExist:
        parent=None
        parent_info=False
    context={
        'student': student,
        'student_info': student_info,
        'subjects': subjects,
        'has_info': has_info,  
        'parent':parent,
        'parent_info':parent_info,
        'student_info_url': reverse('student:studentInfo', kwargs={'pk': pk}) }
    return render(request, 'student/student_profile.html',context )

def studentInfoUpdate(request,pk):
    student=Student.objects.get(pk=pk)
    studentInfo=StudentInfo.objects.get(student_id=pk)
    parentInfo=ParentInfo.objects.get(student_id=pk)

    gender = dob = gaurdian = address = city = district = postal = state = country = None

    if request.method == 'POST':
        gender = request.POST.get('gender')
        if not gender:
            return JsonResponse({'gender_error': 'Invalid gender selected'})

        dob = request.POST.get('dob')
        if not dob:
            return JsonResponse({'dob_error': 'Date of birth is required'})

        gaurdian = request.POST.get('gaurdian').title()
        if gaurdian and not (
            match_expression(expression_full, gaurdian) or match_expression(expression_single, gaurdian)
        ):
            return JsonResponse({'gaurdian_error': 'Invalid gaurdian name'})
        mother_name=request.POST.get('mother').title()
        father_name=request.POST.get('father').title()
        if not (match_expression(expression_single, father_name) or match_expression(expression_full, father_name)):
            return JsonResponse({'father_name_error':True})
        
        email=request.POST.get('email').lower()

        phone=request.POST.get('phone')
        if not (match_expression(expression_number, phone) and len(phone)==10):
            return JsonResponse({'phone_error':True})
        
        address = request.POST.get('address').title()
        if not address:
            return JsonResponse({'address_error': 'Invalid address'})

        city = request.POST.get('city').title()
        if not match_expression(expression_single, city):
            return JsonResponse({'city_error': 'Invalid city name'})

        district = request.POST.get('district').title()
        if not match_expression(expression_single, district) or match_expression(expression_full, city):
            return JsonResponse({'district_error': 'Invalid district name'})

        postal = request.POST.get('postal')
        if not (postal and match_expression(expression_number, postal) and len(postal) == 6):
            return JsonResponse({'postal_error': 'Invalid postal code, must be 6 digits'})

        state = request.POST.get('state').title()
        if not (match_expression(expression_single, state) or  match_expression(expression_full, state)):
            return JsonResponse({'state_error': 'Invalid state name'})

        country = request.POST.get('country').title()
        if not match_expression(expression_single, country) or match_expression(expression_full, country):
            return JsonResponse({'country_error': 'Invalid country name'})

        print(f"Gender: {gender}, DOB: {dob}, gaurdian: {gaurdian}, Address: {address}, "
              f"City: {city}, District: {district}, Postal: {postal}, State: {state}, Country: {country}")
        try:
            exist_email=ParentInfo.objects.filter(email=email).exclude(student_id=pk).first()
            if exist_email:
                return JsonResponse({'email_exist':True})
            else:
                studentInfo.gender=gender
                studentInfo.dob=dob
                studentInfo.gaurdian=gaurdian
                studentInfo.address=address
                studentInfo.city=city
                studentInfo.district=district
                studentInfo.postal_code=postal
                studentInfo.state=state
                studentInfo.country=country
                studentInfo.save()
                #data for parent
                parentInfo.mother_name=mother_name
                parentInfo.father_name=father_name
                parentInfo.parent_phone=phone
                parentInfo.email=email
                parentInfo.address=address
                parentInfo.postal_code=postal
                parentInfo.city=city
                parentInfo.district=district
                parentInfo.country=country
                parentInfo.save()
            return redirect('student:student_profile',pk=pk )

        except Exception as e :
            return JsonResponse({'exception':str(e)})
            

    context={
        'studentInfo':studentInfo,
        'parentInfo':parentInfo,
        'student':student,
        'dob': studentInfo.dob.strftime('%Y-%m-%d') if studentInfo.dob else '',
        'gender':Choice.gender_choice
    }
    return render(request,'student/student_info_form_update.html',context)

def mark_class_attendance(request, class_name):
    if request.method == 'POST':
        students = Student.objects.filter(student_class=class_name)

        for student in students:
            attendance_status = request.POST.get(f"attendance_{student.pk}")
            print(f"Attendance for {student.name}: {attendance_status}")
            
            today = now().date()
            exist_record = Attendence.objects.filter(student_id=student, attendance_date=today).first()
            
            if exist_record:
                return JsonResponse({'attendence already done':True})
            else:
                if attendance_status:
                    Attendence.objects.create(
                        student_id=student,
                        attendance_date=now().date(),
                        attendance_status=attendance_status
                    )
               
        return JsonResponse({'success': True})

    else:
        # Prepare context for the GET request
        choice = Choice.attendance
        AS = [k for k in choice]  # Use list comprehension for simplicity

        context = {
            'students': Student.objects.filter(student_class=class_name),
            'absent': AS[0],
            'present': AS[1],
            'leave': AS[2],
        }
        return render(request, 'student/mark_attendance.html', context)
