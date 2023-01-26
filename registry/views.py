from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request handler- takes a request and gives a response

def say_hello(request):
    return HttpResponse('Hello World')
