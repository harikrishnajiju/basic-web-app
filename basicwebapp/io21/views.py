from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'io21/index.html')

def ourwork(request):
    #return HttpResponse("Hello, world. You're at the io21 our works.")
    return render(request, 'io21/ourworks.html')

def pressreleases(request):
    # return HttpResponse("Hello, world. You're at the io21 press releases.")
    return render(request, 'io21/pressreleases.html')

def contact(request):
    # return HttpResponse("Hello, world. You're at the io21 contact.")
    return render(request, 'io21/contact.html')