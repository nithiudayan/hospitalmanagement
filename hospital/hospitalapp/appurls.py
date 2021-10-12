from django.urls import path
from . views import *
urlpatterns = [
    path('', homePageView, name='home'),
    path('register',register,name='register'),
    path('loginhome',loginhome, name='loginhome'),
    path('patienthome',patienthomepage,name='patienthomepage')
]