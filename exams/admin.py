from django.contrib import admin
from .models import Exam, AdmitCard, Result



class AdmitCardAdmin(admin.ModelAdmin):
    list_display = ('exam_id', 'student_id')
    search_fields = ('exam_id__name', 'student_id__name')
    list_filter = ('exam_id', 'student_id')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('exam_id', 'subject_id', 'student_id', 'attendance_status', 'marks')
    search_fields = ('exam_id__name', 'subject_id__name', 'student_id__name')
    list_filter = ('attendance_status', 'marks')

admin.site.register(AdmitCard, AdmitCardAdmin)
admin.site.register(Result, ResultAdmin)
