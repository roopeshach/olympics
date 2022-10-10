from django.shortcuts import render, redirect
from django.contrib.auth import login , authenticate, logout
from django.core.mail import send_mail
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User
from .models import OTP , PremiumUser
import smtplib, ssl , random
import datetime
# Create your views here.

def mail_sender( email, subject, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "beijingolympics789@gmail.com"
    receiver_email = email
    password = "txhbiocggaiouctu"
    message = message

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message, subject)
        



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
    

#change password 
def change_password(request, id):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = User.objects.get(id=id)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Password Changed Successfully')
        return redirect('Authentication:login')
    else:
        return render(request, 'Authentication/change_password.html')



def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if user.exists():
            user = user[0]
            otp = random.randint(1000, 9999)
            OTP.objects.create(user=user, otp=otp)
            message = f"Your OTP is {otp}"
            mail_sender(email, 'OTP', message)
            messages.add_message(request, messages.SUCCESS, 'OTP Sent to your email')
            return redirect('Authentication:verify-otp', user.id)
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Email')
            return redirect('Authentication:reset-password')
    else:
        return render(request, 'Authentication/reset_password.html')

    
#verify otp and reset password
def verify_otp(request, id):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user = User.objects.get(id=id)
        if OTP.objects.filter(user=user, otp=otp).exists():
            messages.add_message(request, messages.SUCCESS, 'OTP Verified')
            return redirect('Authentication:change-password', id)
        else:
            context = {
                'error' : 'Invalid OTP',
            }
            return render(request, 'Authentication/verify_otp.html', context)
    else:
        return render(request, 'Authentication/verify_otp.html')

def check_user_premium(request):
    user = request.user
    premium_user = PremiumUser.objects.filter(user=user)
    if premium_user.exists():
        return True
    else:
        return False

def user_profile(request):
    user = request.user
    premium_user = PremiumUser.objects.filter(user=user)
    
    if premium_user.exists():
        premium_user = premium_user[0]
        duration = premium_user.duration
        created_at = premium_user.created_at
        expiry_date = created_at + datetime.timedelta(days=0)
        if duration == "1":
            duration = '1 Month'
            price = 100
            expiry_date = created_at + datetime.timedelta(days=30)
        elif duration == "3":
            duration = '3 Months'
            price = 250
            expiry_date = created_at + datetime.timedelta(days=90)
        elif duration == "6":
            duration = '6 Months'
            price = 500
            expiry_date = created_at + datetime.timedelta(days=180)
        elif duration == "12":
            duration = '1 Year'
            price = 1000
            expiry_date = created_at + datetime.timedelta(days=365)


        context = {
            'premium_user': premium_user,
            'duration': duration,
            'expiry_date': expiry_date,
            'price': price,
            
        }
        return render(request, 'Authentication/user_profile.html', context)
    else:
        return render(request, 'Authentication/user_profile.html')
    
