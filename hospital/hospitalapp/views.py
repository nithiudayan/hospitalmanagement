from django.shortcuts import render
from django.http import HttpResponseRedirect
from . models import *

# Create your views here.
from django.http import HttpResponse
def homePageView(request):
    return render(request, "index.html")
def patienthomepage(request):
    return render(request, "patienthome.html")

def register(request):
    if request.method=="POST":
        name = request.POST.get('name')
        addr=request.POST.get('address')
        email = request.POST.get('email')
        mobile=request.POST.get('mobile')
        uname=request.POST.get('username')
        pas=request.POST.get('password')

        l=signin()
        l.username=uname
        l.password=pas
        l.role= 1
        l.save()

        r=registration()

        r.name=name
        r.address=addr
        r.email = email
        r.mobile=mobile
        r.username = uname
        r.password = pas
        r.logid= l
        r.save()
        return HttpResponse("submitted")
    else:
        return render(request,"register.html")

def loginhome(request):
    print("inside login")
    if request.method == "POST":
        uname = request.POST.get('username')
        pas = request.POST.get('password')
        if (signin.objects.filter(username=uname,password=pas).exists()):
            log=signin.objects.filter(username=uname,password=pas)
            request.session['logid'] = log.logid
            request.session['username'] = log.username
            role = log.role
            # return  HttpResponse(role)
            if (role == "admin"):
                return render(request, "AdminHome.html")


            else:
                return render(request, "UserHome.html")
        else:
            message = {'message': "login failed.. try again"}
            return render(request, "index.html", context=message)
    else:
        return render(request, "login.html")


