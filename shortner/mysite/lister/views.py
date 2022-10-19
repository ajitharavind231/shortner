from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from urlshortner.models import urlmodels
from django.views.generic.detail import DetailView

# Create your views here.
#def urllisting(request):
    #return render(request,"urlmodels_list.html")
class urlist(ListView):
    model=urlmodels
    template_name='urlmodels_list.html'

class urldetails(DetailView):
    model=urlmodels
    template_name='urlmodels_detail.html'