from django.contrib import admin
from .models import Student, Subject, Attendence, StudentInfo, ParentInfo, Fee

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'student_class', 'email', 'time','status')
    search_fields = ('name', 'email', 'student_class')
    list_filter = ('student_class', 'status')

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('student_id','subject')
    search_fields = ('student_id__name', 'subject')
    list_filter = ('subject',)

class AttendenceAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'attendance_date', 'attendance_status')
    search_fields = ('student_id__name', 'attendance_date')
    list_filter = ('attendance_status',)

class StudentInfoAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'gender', 'dob', 'gaurdian', 'address', 'city', 'district', 'state', 'country')
    search_fields = ('student_id__name', 'gaurdian', 'city', 'district')

class ParentInfoAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'mother_name', 'father_name', 'parent_phone', 'email', 'address', 'postal_code', 'city', 'district')
    search_fields = ('mother_name', 'father_name', 'email', 'city', 'district')

class FeeAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'fee', 'submitted', 'balance', 'submission_date')
    search_fields = ('student_id__name', 'submission_date')
    list_filter = ('fee', 'submitted', 'balance')

admin.site.register(Student, StudentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Attendence, AttendenceAdmin)
admin.site.register(StudentInfo, StudentInfoAdmin)
admin.site.register(ParentInfo, ParentInfoAdmin)
admin.site.register(Fee, FeeAdmin)
