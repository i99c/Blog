from django.shortcuts import render, redirect
from .forms import *
from .views import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']  # Add email field
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)  # Use email parameter
            user.save()
            messages.success(request, 'Kayıt Başarıyla Tamamlandı')
            return redirect('login')
        else:
            messages.error(request, 'Şifreler Uyuşmuyor')
            return redirect('register')

    return render(request, 'register.html')


def userLogin(request):
    if request.method == "POST":
        email = request.POST['email']  # Add email field
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Başarıyla Giriş Yapıldı')
            return redirect('uyegiris')
        else:
            messages.error(request, 'Kullanıcı Adı veya Şifre Yanlış')
            return redirect('login')

    return render(request, "login.html")


def userLogout(request):
    logout(request)
    messages.success(request, 'Başarıyla Çıkış Yapıldı')
    return redirect('index')

def index(request):
    return render(request, "index.html")

def uyegiris(request):
    return render(request, 'uyegiris.html')