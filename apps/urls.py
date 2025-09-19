from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('signin/',views.user_signin,name='signin'),
    path('logout/',views.user_logout,name='logout'),
    path('dashbord/',views.dash_bord,name='dashbord'),
]