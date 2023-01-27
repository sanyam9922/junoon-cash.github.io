from django.shortcuts import render, HttpResponse
from datetime import datetime
from Home.models import Contact
# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def advice(request):
     return render(request, 'advice.html')     

def prices(request):
     return render(request, 'prices.html')

def learn(request):
     return render(request, 'learn.html') 

def returns(request):
    return render(request, 'returns.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, message=message, date = datetime.today())
        contact.save()
        return render(request, 'submitted.html')

    return render(request, 'contact.html')

def forex(request):
    return render(request, 'forex.html')    
 
