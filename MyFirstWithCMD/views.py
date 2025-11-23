from django.shortcuts import render
from django.http import HttpResponse

def about(request):
    # return HttpResponse("Hello EveryOne")
    return render(request, 'about.html')
def home(response):
    # return HttpResponse('Welcome to my Home Page!')
    return render(request,'home.html')