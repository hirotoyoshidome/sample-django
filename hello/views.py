from django.shortcuts import render
from django.http import HttpResponse

def hello(req):
    body = "Hello World!!!\n"
    print(type(req))
    return HttpResponse(body)

# Create your views here.
