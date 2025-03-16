from django.urls import path
from . import views
app_name='admins'
urlpatterns=[
	path('dashboard/board_list',views.Education_board_view,name='board_list'),
    path('dashboard/<int:pk>/delete/',views.Education_board_delete,name='board_delete'),
    path('dashboard/<int:pk>/update/',views.Education_board_update,name='board_update'),
    path('dashboard/board_add/',views.Education_board_add,name='board_add'),
	path('dashboard/year_view',views.Education_year_view,name="year_view"),
    path('dashboard/year_add',views.Education_year_add,name="year_add"),
    path('dashboard/<int:pk>/year-update/',views.Education_year_update,name="year_update"),
    path('dashboard/<int:pk>/year_delete/',views.Education_year_delete,name="year_delete"),
    path('dashboard/exam_view',views.Exam_view,name='exam_view'),
    path('dashboard/exam_add',views.Exam_add,name='exam_add'),
    path('dashboard/<int:pk>/exam_update',views.Exam_update,name='exam_update'),
    path('dashboard/<int:pk>/exam_delete',views.Exam_delete,name='exam_delete'),

    
] 
