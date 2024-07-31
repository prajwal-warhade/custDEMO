from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile
from django.db import IntegrityError
from django.contrib.auth.hashers import make_password
from django.views import View

class SignInView(View):
    def get(self, request):
        return render(request, 'user_login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('user_password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'user_login.html', {'errmsg': 'Invalid credentials'})

class SignUpView(View):
    def get(self, request):
        return render(request, 'user_login.html')

    def post(self, request):
        email = request.POST.get('user_email')
        username = request.POST.get('username')
        password = request.POST.get('user_password')
        confirm_password = request.POST.get('user_password_confirm')

        if not (email and username and password and confirm_password):
            return render(request, 'user_login.html', {'errmsg': 'Fields cannot be blank'})
        elif password != confirm_password:
            return render(request, 'user_login.html', {'errmsg': 'Password and Confirm Password do not match'})
        elif len(password) < 8:
            return render(request, 'user_login.html', {'errmsg': 'Password must be at least 8 characters'})
        else:
            try:
                # Hash the password before saving
                hashed_password = make_password(password)
                user = User.objects.create(email=email, username=username, password=hashed_password)
                UserProfile.objects.create(user=user, email=email)
                return redirect('sign_in')
            except IntegrityError:
                return render(request, 'user_login.html', {'errmsg': 'User already exists'})
            except Exception as e:
                return render(request, 'user_login.html', {'errmsg': 'An error occurred during registration: ' + str(e)})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/user/sign-in')
