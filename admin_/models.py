from django.db import models
from django.utils import timezone
from home.models import Choice
# Create your models here.
class EducationalBoard(models.Model):
    education_Board_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    def __str__(self):
        return(f'{self.name}')
    class Meta:
        db_table='EducationalBoard'
class EducationalYear(models.Model):
    education_year_id=models.AutoField(primary_key=True)
    year=models.CharField(max_length=32,default='')
    def __str__(self):
        return(f'{self.year}')
    class Meta:
        db_table='EducationalYear'


class Exam(models.Model):
    Exam_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32)
    exam_type=models.CharField(max_length=32)
    date=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.name} "
    class Meta:
        db_table='Exam'