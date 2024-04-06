from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('register/', userRegister, name='register'),
    path('login/', userLogin, name="login"),
    path('uyegiris/', uyegiris, name='uyegiris'),
    path('logout/', userLogout, name='logout'),
    
]