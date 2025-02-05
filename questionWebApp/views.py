from django.shortcuts import render


def homepage(request):
    return render(request, 'questionwebapp/homepage.html')

def contact(request):
    return render(request,'questionwebapp/contact.html')

def about(request):
    return render(request,'questionwebapp/about.html')

def blog(request):
    return render(request,'questionwebapp/blog.html')

def services(request):
    return render(request,'questionwebapp/services.html')