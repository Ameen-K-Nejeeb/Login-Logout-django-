from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    messages.success(request,"You have veen logged out!")
    return redirect('login')

def user_signin(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request,'Invalid username or password')
            return redirect('signin')
        
        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already exists!")
            return redirect('signin')
        user = User.objects.create_user(username = username, password = password1)
        user.save()
        messages.success(request, "Account created successfully! please login.")
        return redirect('login')

    return render(request,'signin.html')


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        #check critential
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user) #create session
            messages.success(request, f'Welcome {user.username}!')
            return redirect('dashbord')
        else:
            messages.error(request, 'Invalid username or password(Try again!)')
            return redirect('login')


    return render(request, 'login.html')

# Dashboard (protected)
@login_required(login_url='login')
def dash_bord(request):
    return render(request, 'dashboard.html', {"username": request.user.username})
