from django.urls import path
from .views import sign_in, sign_up, user_logout

urlpatterns = [
    path('sign-in/', sign_in, name='sign_in'),  
    path('sign-up/', sign_up, name='sign_up'),
    path('logout/', user_logout, name='logout'),
]


