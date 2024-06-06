from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    path('admin/',include('cust_admins.urls')),
    path('dev-admin/', admin.site.urls),
    path('',include('dashboard.urls')),
]
