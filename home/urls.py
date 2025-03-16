from django.urls import path
from . import views
app_name='home'
urlpatterns = [
    #home 
    path('home/',views.user_query),
    path('dashboard/add_user',views.user_add,name='add_user'),
    path('dashboard/update_user/<str:pk>/',views.user_update,name='update_user'),
    path('stateless/',views.stateless),
    path('thanks/',views.thanks),
    path('registration/',views.user_registration),
    path('login/',views.login)

]
