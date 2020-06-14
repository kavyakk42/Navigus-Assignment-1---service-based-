from django.shortcuts import render
from first.models import Register
from first.models import Active
from django.http import HttpResponse
from django.shortcuts import redirect
import requests
import json
import datetime
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
# Create your views here.
def reg(request):
    if request.method == 'POST':
        mail=request.POST.get('email')
        user=Register.objects.filter(email=mail)
        print(user)
        if(len(user)>0):
            s='Email is Already Registered'
            return render(request,'reg.html',{'s':s})
        else:
            pas=request.POST.get('pass')
            pas1=request.POST.get('pass1')
            if pas==pas1:
                reg=Register()
                reg.name= request.POST.get('name')
                reg.email= request.POST.get('email')
                reg.password= request.POST.get('pass')
                reg.gender= request.POST.get('gender')
                reg.coun= request.POST.get('country')
                reg.img= request.POST.get('avatar')
                reg.save()
                return redirect(login)
            else:
                p='Passwords Do not Match'
                return render(request,'reg.html',{'s':p})
    else:
        return render(request,'reg.html')

def logout(request):
	uname=request.session['s_name']
	print(uname)
	Active.objects.filter(email=uname).delete()
	del request.session['s_name']
	return redirect(login)

def login(request):
	if request.method =='POST':
		formpost=True
		username=request.POST.get('email')
		password=request.POST.get('password')
		errormsg=""
		cred=Register.objects.filter(email=username,password=password)
		k=len(cred)
		if k>0:
			print("Valid Credentials")
			request.session['s_name']=username
			user=Active.objects.filter(email=username)
			print(user)
			if(len(user)>0):
				print("exist")
			else:
				act=Active()
				act.email=username
				now = datetime.datetime.now()
				time=now.time
				act.date=now
				act.save()
			return redirect(dashboard)
		else:
			print("Invalid Credentials")
			errormsg="Invalid Credentials"
			return render(request,"newlogin.html",{'formpost':formpost})
	else:
		formpost=False
		return render(request,"newlogin.html",{'formpost':formpost})


def dashboard(request):
	if not request.session.has_key('s_name'):
		return redirect(login)
	else:
		cp=Register.objects.get(email=request.session['s_name'])
		u=cp.name
		all_entries = Active.objects.all()
		alln = Active.objects.values('email','date').all()
		return render(request,'dashboard.html',{'user':all_entries,'n':u,'alln':alln})

def time(request):
	if not request.session.has_key('s_name'):
		return redirect(login)
	else:
		alle=Active.objects.values('email','date').all()
		print(alle)
		return render(request,'time.html',{'obj':alle})