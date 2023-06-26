from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    return HttpResponse('Say Hello')
# Create your views here.
