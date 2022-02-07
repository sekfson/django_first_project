from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_view,name="home"),
    path('room/',views.room_view,name="room"),
    path('create-room/',views.createRoom,name='create-room'),
    path('update-room/<int:pk>/',views.updateRoom,name='update-room'),
    path('delete-roo/<str:pk>/',views.deleteRoom,name="delete-room"),
]