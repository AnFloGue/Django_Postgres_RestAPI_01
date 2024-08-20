# world_countries/urls.py

from django.contrib import admin
from django.urls import path, include
from countries.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('countries/', include('countries.urls')),
    path('', index, name='index'),  # Add this line
]