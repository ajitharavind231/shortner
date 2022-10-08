import random
from django import http
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import urlmodels
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth.models import User

def longpage(request):
    return render(request,'long.html')

@csrf_exempt  
def shorturl(request):
    if request.method=='POST':
        longurl=request.POST['longurl']
        soruce="abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*"
        shorturl=("".join(random.sample(soruce,7)))
        obj=urlmodels.objects.create(longurl=longurl,shorturl=shorturl)
        #shorturl='http://localhost:8000/short'+shorturl
    return HttpResponse("<h3>your shorturl for</h3> {} <br> is <br> http://localhost:8000/short/{}".format(longurl,shorturl))
    
def redirecturl(request,shorturl):
    print(shorturl)
    obj=urlmodels.objects.get(shorturl=shorturl)
    print("the long url is ",obj.longurl)
    #expiry = timezone.now().date() - timedelta(days=7)
   # obj=urlmodels.objects.filter(added=expiry)
    if obj:
    
        return redirect('https://'+obj.longurl)
    else:
        return Http404