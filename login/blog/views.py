from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	return render(request,"blog/index.html")

def login(request):
	if request.method=='POST':
			username = request.POST["username"]
			password = request.POST["password"]
			user = auth.authenticate(username=username,password=password)
			if user is not None:
				auth.login(request,user)
				return redirect("/profile/{num}".format(num = user.id))
			else:
				messages.info(request,"Invalid credintals")
				return redirect("/login")
			return render(request,'login.html')
	return render(request,'login.html')


def register(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			form.save()
			return redirect("/login")
		else:
			messages.info(request," Please Enter valid data")
	else:
		form = RegisterForm()

	return render(request,"register.html",{"form":form})

@login_required(login_url='/login')
def profile(request,id):
	user=User.objects.filter(id=id)
	return render(request,"profile.html",{'user':user})

	
