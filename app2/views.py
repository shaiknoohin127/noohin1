from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def shaik(request):
    return HttpResponse("shaik is best")