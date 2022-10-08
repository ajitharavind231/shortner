from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def loginpage(request):
   return render(request,"login.html")