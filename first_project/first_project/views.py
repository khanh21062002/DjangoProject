from django.http import HttpResponse
from django.shortcuts import  render

def  Homepage(request):
    return render(request, 'home.html')
    # return HttpResponse("Hello, World! This is my first Django project.")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")

def blog(request):
    return HttpResponse("This is the blog page.")