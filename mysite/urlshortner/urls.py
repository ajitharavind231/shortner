from django.shortcuts import redirect
from django.urls import URLPattern, path
from . import views

urlpatterns=[
    path('',views.longpage,name='shortner'),
    path('shorter/',views.shorturl),
    path('<str:shorturl>',views.redirecturl,name="redirect"),

]
