from django.contrib import admin
from request.models import QueryRequest, Complaint

class QueryRequestAdmin(admin.ModelAdmin):
    list_display = ('name','email','time')
    search_fields = ('name', 'email')
    list_filter = ('time',)

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','time')
    search_fields = ('name', 'email')
    list_filter = ('time',)

admin.site.register(QueryRequest, QueryRequestAdmin)
admin.site.register(Complaint, ComplaintAdmin)
