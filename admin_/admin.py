from django.contrib import admin
from .models import EducationalBoard, EducationalYear,Exam
class EducationalBoardAdmin(admin.ModelAdmin):
    list_display = ('education_Board_id', 'name')
    search_fields = ('name',)
    
class EducationalYearAdmin(admin.ModelAdmin):
    list_display = ('education_year_id', 'year')
    search_fields = ('year',)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('Exam_id', 'name', 'exam_type', 'date')
    search_fields = ('name', 'exam_type')
    list_filter = ('date',)

admin.site.register(Exam, ExamAdmin)
admin.site.register(EducationalBoard, EducationalBoardAdmin)
admin.site.register(EducationalYear, EducationalYearAdmin)
