from django.shortcuts import render
from users.models import UserProfile
from products.models import Product 


def Home(request):

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        products = Product.objects.filter(is_active=True)
        context = {
            'prod': products,
            'data1': user_profile
        }
    else:
        products = Product.objects.filter(is_active=True)
        context = {'prod': products}
    return render(request,'carousel.html',context)




def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Gallery(request):
    return render(request,'gallery.html')
