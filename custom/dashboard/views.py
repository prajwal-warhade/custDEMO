from django.shortcuts import render

def Home(request):
    return render(request,'carousel.html')

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def Gallery(request):
    return render(request,'gallery.html')
