from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_login(request):
    return render(request,'login.html')

def user_signin(request):
    return render(request,'signin.html')

def user_logout(request):
    return render(request, 'logout.html')

def dash_bord(request):
    return render(request, 'dashbord.html')