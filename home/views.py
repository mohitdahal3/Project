from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'home/home.html')

def services(request):
    return render(request , 'home/services.html')

def courses(request):
    return render(request , 'home/courses.html')

def videos(request):
    return render(request , 'home/videos.html')

def contact(request):
    return render(request , 'home/contact.html')

def help(request):
    return render(request , 'home/help.html')

def joinus(request):
    return render(request , 'home/join.html')