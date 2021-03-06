"""gym_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.applicant_list, name='applicant_list'),
    path('applicant/<uuid:pk>/', views.applicant_detail, name='applicant_detail'),
    path('applicant/edit/<uuid:pk>/', views.applicant_edit, name='applicant_edit'),
    path('applicant/new/', views.applicant_new, name='applicant_new'),
    path('payment/', views.applicant_pay, name='applicant_pay'),
    path('plan/new/', views.plan_new, name='plan_new'),
    path('plan/', views.plan_list, name='plan_list'),
]
