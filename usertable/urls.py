from django.urls import path
from . import views
app_name='user_table'
urlpatterns=[
    path('dashboard/user',views.user_view,name='view_user'),
    path('dashboard/user_delete/<str:pk>/',views.user_delete,name='user_delete'),

]