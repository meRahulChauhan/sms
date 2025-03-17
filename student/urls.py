from django.urls import path
from . import views
app_name='student'
urlpatterns = [
   # path('dashboard/',views.student_list_view),
    path('dashboard/student_all',views.student_list_view,name='student_list'),
    path('dashboard/student_view/<str:pk>/',views.student_view_by_class,name='student_by_class'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),
    path('students/<int:pk>/update/', views.student_update, name='student_update'),
    path('dashboard/add_student/',views.add_student,name='add_student'),
    path('dashboard/student/subject/<str:pk>/',views.save_subject,name='save_subject'),
    path('dashboard/student/profile/<str:pk>/',views.student_profile,name='student_profile'),
    path('dashboard/student/studentInfo/<str:pk>/',views.studentInfo,name='studentInfo'),
    path('dashboard/student/parentInfo/<str:pk>/',views.studentInfo,name='parentInfo'),
    path('dashboard/student/studentInfoUpdate/<str:pk>/',views.studentInfoUpdate,name='studentInfoUpdate'),
    path('dashboard/student/attendance/<str:class_name>/', views.mark_class_attendance, name='mark_class_attendance'),
    #path('dashboard/exam_view',views.Exam_view)

]
