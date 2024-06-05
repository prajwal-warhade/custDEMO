from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')
        
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_data = User.objects.filter(username=username)
        
            if user_data.exists():  # Check if user data exists in the database
                user_data = authenticate(username=username, password=password)
                
                if user_data and user_data.is_superuser:
                    login(request, user_data)
                    return redirect('dashboard/')
                else:
                    messages.info(request, "Invalid username or password")
                    return redirect('/')
            else:
                messages.info(request, "User does not exist")
                return redirect('/')
        
        return render(request, "admin_login.html")
    
    except Exception as e:
        print(e)
        return HttpResponse('Something went wrong')
    

def admin_dashboard(request):
    return render(request, "admin_dashboard.html")