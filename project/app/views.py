from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def func1(request):
    return HttpResponse("<h1>Welcome</h1>")
def func2(request,data):
    return HttpResponse(data)
    