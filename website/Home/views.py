from django.shortcuts import render, HttpResponse
from Home.models import Contact
from datetime import datetime 
from django.contrib import messages

# Create your views here.
def index(request):
   return render(request,'index.html')
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact=Contact(name=name,email=email,message=message)
        contact.save()
        message.success(request,"Your Message has been sent Successfully!")
    return render(request,"contact.html")