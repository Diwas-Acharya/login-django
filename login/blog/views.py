from django.shortcuts import render ,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def index(request):
	return render(request,"blog/index.html")

def login(request):
	return render(request,"login.html")


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			return redirect("/login")
			print("user created")
		else:
			print("something wrong")
	else:
		form = RegisterForm()

	return render(request,"register.html",{"form":form})

	
