from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'About.html')

def service(request):
    return render(request,'service.html')

def navbar(request):
    return render(request,'navbar.html')

def traffic(request):
    return render(request,'traffic.html')

def contaner1(request):
    return render(request,'contaner1.html')
 
def contaner2(request):
    return render(request,'contaner2.html')

def contact(request):
    return render(request,'contact.html')

def footer(request):
    return render(request, 'footer.html')