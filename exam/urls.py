from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('linux', include('linux.urls')),
    path('nca/', include('nca.urls')),
    path('aws/', include('aws.urls')),
    path('', include('home.urls')),
] 
