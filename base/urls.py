from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('contact/<int:pk>/',views.contact_view,name="com"),
]
