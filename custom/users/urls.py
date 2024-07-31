from django.urls import path
from .views import SignInView, SignUpView, LogoutView

urlpatterns = [
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
