from django.shortcuts import render
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,"home.html")

def price(request):
    return render(request,"price1.html")

def contactus(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        phoneNumber=request.POST.get('phoneNumber')
        complain=request.POST.get('complain')
        date=datetime.today()
        contact=Contact(first_name=first_name,last_name=last_name,email=email,phoneNumber=phoneNumber,complain=complain,date=date)
        contact.save()  
        if(complain!=0):
            messages.success(request,'Your response is submitted!') 

    return render(request,"contactUs.html")