from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser, name= 'loginuser'),
    path('home/', views.home, name='home'),
    path('add_emp/', views.add_emp, name='add_emp'),
    path('view_emp/', views.view_emp, name='view_emp'),
    path('manager_info/', views.manager_info, name='manager_info'),
    path('department/', views.department, name='department'),
    path('update_employee/<int:pk>', views.update_employee, name='update_employee'),
    path('delete_employee/<int:emp_id>', views.delete_employee, name='delete_employee'),
    
]