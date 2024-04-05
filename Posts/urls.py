from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index.html"),
    path('uyegiris/', uyegiris, name="uyegiris"),
]
