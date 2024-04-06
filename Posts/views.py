from django.shortcuts import render
from .models import Post

def index(request):
    return render(request, "index.html")

def uyegiris(request):
    return render(request, 'uyegiris.html')



def uyegiris(request):
    trend_konular = Post.objects.order_by('-view_count')[:5]
    son_gonderiler = Post.objects.order_by('-created_at')[:10]
    return render(request, 'uyegiris.html', {'trend_konular': trend_konular, 'son_gonderiler': son_gonderiler})