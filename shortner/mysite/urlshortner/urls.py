from django.shortcuts import redirect
from django.urls import URLPattern, path
from . import views
#from .views import Dyt

urlpatterns=[
    path('',views.longpage,name='shortner'),
    path('main/',views.one1,name="maane"),
    path('shorter/',views.shorturl),
    path('<str:shorturl>',views.redirecturl,name="redirect"),
    #path('detail',views.details)
    #path('detail/',Dyt.as_view(),name='detailer')

]
