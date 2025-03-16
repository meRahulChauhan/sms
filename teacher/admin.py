from django.contrib import admin
from .models import teacher

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_id', 'name', 'gender', 'specialization_in', 'phone', 'email')
    search_fields = ('name', 'email', 'specialization_in')
    list_filter = ('gender', 'specialization_in', 'time')


admin.site.register(teacher, TeacherAdmin)
