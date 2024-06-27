from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile
from django.db import IntegrityError
from django.http import HttpResponse

def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('user_password')
        print(username, password)
        
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'user_login.html', {'errmsg': 'Invalid credentials'})
    return render(request, 'user_login.html')

def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        username = request.POST.get('username')
        password = request.POST.get('user_password')
        confirm_password = request.POST.get('user_password_confirm')
        #print(email, username, password, confirm_password)
        
        
        if not (email and username and password and confirm_password):
            return render(request, 'user_login.html', {'errmsg': 'Fields cannot be blank'})
        elif password != confirm_password:
            return render(request, 'user_login.html', {'errmsg': 'Password and Confirm Password do not match'})
        elif len(password) < 8:
            return render(request, 'user_login.html', {'errmsg': 'Password must be at least 8 characters'})
        else:
            try:
                user = User.objects.create(email=email ,username=username, password=password)
                UserProfile.objects.create(user=user, email=username)
                return redirect('sign_in')
            except IntegrityError:
                return render(request, 'user_login.html', {'errmsg': 'User already exists'})
            except Exception as e:
                return render(request, 'user_login.html', {'errmsg': 'An error occurred during registration: ' + str(e)})
    return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('/user/sign-in')
