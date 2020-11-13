from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_page,name='home'),
    path('customer/<int:pk>',customer_page,name='customer'),
    path('service/',service_page,name='service'),
    path('feedback/',feedback_page,name='feedback'),
    path('contact/',contact_page,name='contact'),
    path('master/',master_page,name='master'),
    path('certificate/',certificate_page,name='certificate'),
    path('service/<int:pk>/',service_detail,name='detail'),
    path('master/<int:pk>/',master_detail,name='master_details'),
    path('register/',register,name='register'),


]