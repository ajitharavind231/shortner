from django.shortcuts import redirect
from django.urls import URLPattern, path
from . import views
from .views import urlist,urldetails

urlpatterns=[
    path('',urlist.as_view(),name='lister'),
    path('lists/<int:pk>/',urldetails.as_view(),name='detailer')

]