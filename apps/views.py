from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache




# Create your views here.
# @never_cache
# def home(request):
#     return render(request, 'home.html')

@never_cache
def user_logout(request):
    logout(request)
    messages.success(request,"You have been logged out!")
    return redirect('login')

@never_cache
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

@never_cache
def user_login(request):

    if request.user.is_authenticated:
         return redirect('dashbord')

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
@never_cache
@login_required(login_url='login')
def dash_bord(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'dashbord.html', {"username": request.user.username})
