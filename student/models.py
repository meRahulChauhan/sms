from django.db import models
from django.urls import reverse
from django.utils import timezone
from home.models import Choice
#from teacher.models import teacher
from admin_.models import EducationalBoard,EducationalYear        

class Student(models.Model):
    educational_Board_id=models.ForeignKey(EducationalBoard,on_delete=models.CASCADE)
    year=models.ForeignKey(EducationalYear,on_delete=models.CASCADE)
    student_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=64)
    student_class=models.CharField(max_length=5,choices=Choice.class_choice)
    #teacher=models.ForeignKey(teacher,on_delete=models.PROTECT)
    email=models.CharField(max_length=64,unique=True)
    time=models.DateTimeField(default=timezone.now)
    status=models.CharField(max_length=2,choices=Choice.status)
    class Meta:
        db_table='Student'
        ordering=['name']
    def __str__(self):
        return f"{self.name},C-{self.student_class},id- {self.student_id},@- {self.email};"
   
class Subject(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    subject_id=models.AutoField(primary_key=True)
    subject=models.CharField(max_length=32,blank=False)
    def __str__(self):
        return f"{self.student_id} {self.subject}"
    class Meta:
        db_table='Subject'
        
class Attendence(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    attendance_date=models.DateTimeField(default=timezone.now)
    attendance_status=models.CharField(max_length=10,choices=Choice.attendance)
    def __str__(self):
        return f'{self.student_id},{self.attendance_date},{self.attendance_status}'
    class Meta:
        db_table='Attendence'

class StudentInfo(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    student_img=models.ImageField(blank=True)
    gender=models.CharField(max_length=1,choices=Choice.gender_choice)
    dob=models.DateField(null=True)
    gaurdian=models.CharField(max_length=64,null=True)
    address=models.CharField(max_length=64,null=True)
    city=models.CharField(max_length=64,null=True)
    district=models.CharField(max_length=64,null=True)
    postal_code=models.CharField(max_length=6,blank=True)
    state=models.CharField(max_length=64,null=True)
    country=models.CharField(max_length=64,null=True)
    
    def __str__(self):
        return f"{self.student_id}"
    class Meta:
        db_table='StudentInfo'
        ordering=['id']

class ParentInfo(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    mother_name=models.CharField(max_length=64,null=True)
    father_name=models.CharField(max_length=64,null=True)
    parent_phone=models.CharField(max_length=10,null=True)
    email=models.EmailField(max_length=64,primary_key=True)
    address=models.CharField(max_length=64,null=True)
    postal_code=models.CharField(max_length=6,null=True)
    city=models.CharField(max_length=64,null=True)
    district=models.CharField(max_length=64,null=True)
    country=models.CharField(max_length=64,null=True)
    class Meta:
        db_table='ParentInfo'
class Fee(models.Model):
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    fee=models.CharField(max_length=4,default='')
    submitted=models.CharField(max_length=4,default='')
    balance=models.CharField(max_length=4,default='')
    submission_date=models.DateTimeField(default=timezone.now)
    class Meta:
        db_table='fee'        
