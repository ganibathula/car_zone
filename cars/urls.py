from django.urls import path
from .views import *

urlpatterns=[
    path('cars',car_view,name='cars')
]