from django.contrib import admin
from .models import usertable

# Register your models here.
class UsertableAdmin(admin.ModelAdmin):
	list_display=['name','email','created_at']
	list_filter=('name','email','created_at',)
	ordering=['created_at']
	list_display=['name','email','created_at']
admin.site.register(usertable,UsertableAdmin)	
