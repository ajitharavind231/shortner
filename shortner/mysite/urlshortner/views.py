from cgitb import reset
from pickle import OBJ
import random
from django import http
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import urlmodels
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic.list import ListView

def longpage(request):
    return render(request,'long.html')
    

@csrf_exempt  
def shorturl(request):
    if request.method=='POST':
        longurl=request.POST['longurl']
        if longurl is None:    
            return HttpResponse('sorry the string is null')
        else:
            #longurl=request.POST['longurl']
            soruce="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*"
            shorturl=("".join(random.sample(soruce,7)))
            obj=urlmodels.objects.create(longurl=longurl,shorturl=shorturl)
            #shorturl='http://localhost:8000/short'+shorturl
    return HttpResponse("<h3>your shorturl for</h3> {} <br> is <br> http://localhost:8000/short/{}".format(longurl,shorturl))
    
def redirecturl(request,shorturl):
    print(shorturl)
    try:
        obj=urlmodels.objects.get(shorturl=shorturl)
    except urlmodels.DoesNotExist:
        obj= None

    if obj is not None:
        obj.count+=1
        obj.save()
        return redirect('https://'+obj.longurl)
    else:
        return HttpResponse("This is not linked to any website")



def one1(request):
    return HttpResponse("this is not working")
   
