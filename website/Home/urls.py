from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
 path('',views.index,name='Home'),
 path('About/',views.about,name='About'),
 path('Contact/',views.contact,name='Contact')
]
