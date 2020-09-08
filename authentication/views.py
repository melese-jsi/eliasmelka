from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from authentication.forms import SignupForm
#from authentication.models import User



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home/')
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password")
            return render(request, 'authentication/login.html')

    else:
        return render(request,'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if not form.is_valid():
            messages.add_message(request,messages.ERROR,'Error while creating user account. please check all fields and try again')
            return render(request,'authentication/signup.html',{'form':form})
        else:
            screen_name =form.cleaned_data.get('screen_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            get_user_model().objects.create_user(username=username,email=email,password=password,screen_name=screen_name)
            user= authenticate(username=username,password=password)
            login(request,user)
            messages.add_message(request,messages.SUCCESS,"Your account is successfully created")
            return HttpResponseRedirect('/home/')




    else:
        form = SignupForm()
        return render(request,'authentication/signup.html',{'form':form})

def signout(request):
    logout(request)
    return HttpResponseRedirect('/home/')
def reset(request):
    pass

