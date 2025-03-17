from django.db import models
from django.db import models
from django.utils import timezone
from home.models import Choice
from django.contrib.auth.hashers import make_password

class teacher(models.Model):
    teacher_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=64,blank=False)
    gender=models.CharField(max_length=1,choices=Choice.gender_choice)
    specialization_in=models.CharField(max_length=15,choices=Choice.specialization_choice)
    phone=models.CharField(max_length=12,blank=True)
    email=models.EmailField(max_length=64)
    password=models.CharField(max_length=128,default='')
    time=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"name-{self.name},email-{self.email},phone-{self.phone}"
    class Meta:
        db_table='teacher'
