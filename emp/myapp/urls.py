from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name= 'loginuser'),
    path('home/', views.home, name='home'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('view_emp/', views.view_emp, name='view_emp'),
    path('grievances/', views.grievances, name='grievances'),
    path('manager_info/', views.manager_info, name='manager_info'),
    path('department/', views.department, name='department'),
]