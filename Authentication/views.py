from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate, logout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User
# Create your views here.

def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password= password)

            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login Successful')
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Invalid Credentials')
                return redirect('/login')
        else:
            return render(request, 'Authentication/login.html')
    

def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Registration Successful')
                return redirect('/login')
            else:
                messages.add_message(request, messages.ERROR, 'Error Registering User')
                return redirect('/register')
        else:
            form = UserForm()
            context = {
                'form': form
            }
            return render(request, 'Authentication/register.html', context)

def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout Successful')
    return redirect('/login')


