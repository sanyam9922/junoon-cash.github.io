from django.shortcuts import render, HttpResponse

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
    return render(request, 'contact.html')

def forex(request):
    return render(request, 'forex.html')    
 
