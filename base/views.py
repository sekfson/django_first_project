from this import d
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .models import Romm

rooms=[
    {'id':1 ,'name':'kourouma'},
    {'id':2,'name':'balde'},
    {'id':3,'name':'bangoura'},
]

def home_view(request):
    return render(request,'home.html')



def room_view(request,pk):
    rooms=Romm.objects.all()   
    context={'rooms':rooms}
    return render(request,'base/room.html',context)