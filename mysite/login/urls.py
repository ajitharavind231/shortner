from django.shortcuts import redirect
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path("",views.loginpage,name="loginer")
]