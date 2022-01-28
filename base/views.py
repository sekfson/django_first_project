from this import d
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.template import context

contacts=[
    {'id':1 ,'name':'kourouma'},
    {'id':2,'name':'balde'},
    {'id':3,'name':'bangoura'},
]

def home_view(request):
    return render(request,'home.html')



def contact_view(request,pk):
    contact=None
    for i in contacts:
        if i['id']== int(pk):
            contact=i    
    context={'contacts':contacts}
    return render(request,'base/contact.html',context)