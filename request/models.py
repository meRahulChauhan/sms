from django.db import models
from django.db import models
from django.utils import timezone

class QueryRequest(models.Model):
    #types=models.CharField(max_length=4,choices=Choice.types)
    #phone = models.CharField(max_length=12,blank=False)
    #subject = models.CharField(max_length=255,blank=False)
    name = models.CharField(max_length=255,blank=False)
    email = models.EmailField(max_length=255,blank=False)
    body = models.TextField(blank=False)
    time = models.DateTimeField(default=timezone.now)
    class Meta:
        db_table = 'query_request'
    def __str__(self):
        return(f'Name:{self.name},Email: {self.email};')

class Complaint(models.Model):
    name = models.CharField(max_length=255)
    #phone = models.CharField(max_length=12,default=False)
    #subject = models.CharField(max_length=255)
    email = models.EmailField()
    #img = models.ImageField(upload_to='images')
    body = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table='complain'


