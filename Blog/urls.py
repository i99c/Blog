from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Posts.urls')),
    path('user/', include('User.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
