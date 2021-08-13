from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def noohin(request):
    return HttpResponse('<center><h1 style="color:blue;">BEAUTIFUL</h1></center>')