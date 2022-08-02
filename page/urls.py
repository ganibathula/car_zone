from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('about/',about_page,name='about'),
    path('service/',service_page,name='service'),
    path('contact/',contact_page,name='contact'),
]