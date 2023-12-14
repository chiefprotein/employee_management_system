from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser),
    path('home/', views.home, name='home'),
    path('add_emp/', views.add_emp),
]