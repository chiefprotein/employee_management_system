from django.urls import path
from . import views

urlpatterns = [
    path('', views.login),
    path('home/', views.home),
    path('add_emp/', views.add_emp),
]