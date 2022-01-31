from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('room/<int:pk>/',views.room_view,name="com"),
    path('create-room',views.createRoom,name='create-room')

]