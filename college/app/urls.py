from django.urls import path
from .views import *


urlpatterns = [
    path('',home, name="home"),
    path('allpapers',allpapers,name='allpapers'),
    path('uploadnew',newpaper,name='newpaper'),
    path('contact',contact,name="contact"),
    path('search/',search,name="search"),
]
