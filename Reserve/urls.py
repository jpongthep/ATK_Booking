from django.urls import path
from django.shortcuts import render

from .views import  Booking, Search_Page

app_name = 'Reserve'
urlpatterns = [
    path('booking',Booking, name = 'booking'),
    path('search',Search_Page, name = 'search')

]
