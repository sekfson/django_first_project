from this import d
from unicodedata import name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import context
from .models import Room
from .forms import RoomForm


def home_view(request):
    return render(request,'home.html')



def room_view(request,pk):
    rooms=Room.objects.all()   
    context={'rooms':rooms}
    return render(request,'base/room.html',context)

def createRoom(request):
    form=RoomForm
    if request.method=='POST':
        form=RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html', context)


def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form =RoomForm(instance=room)

    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'base/room_form.html',context)
