from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import usertable
import re

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

def user_view(request):
    usr=usertable.objects.all()
    return render(request,'usertable/user_view.html',{'usr':usr})

def user_delete(request,pk):
    usr=usertable.objects.get(pk=pk)
    if request.method=='POST':
        usr.delete()
        return redirect('user_table:view_user')
    return render(request,'usertable/user_delete.html')
