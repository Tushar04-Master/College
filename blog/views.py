from django.shortcuts import render
from django.http import HttpResponse

def myblog(request):
    return HttpResponse("This is my blog")
