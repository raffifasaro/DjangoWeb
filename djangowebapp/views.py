from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request handler

def print_hi(request):
    return HttpResponse('hi')
