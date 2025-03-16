from django.db import models
from django.db import models
from django.utils import timezone
from home.models import Choice
from student.models import Student,Subject
from admin_.models import Exam



class AdmitCard(models.Model):
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    class Meta:
        db_table='AdmitCard'

class Result(models.Model):
    exam_id=models.ForeignKey(Exam,on_delete=models.CASCADE)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    student_id=models.ForeignKey(Student,on_delete=models.CASCADE)
    #invigilator=models.CharField(max_length=32,default='-na')
    attendance_status=models.CharField(max_length=10,choices=Choice.attendance)
    marks=models.IntegerField()
    class Meta:
        db_table='Result'
    def __str__(self):
        return (f'{self.attendance_status}')

        

