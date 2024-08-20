from django.urls import path
from . import views
from .views import countries_list

urlpatterns = [
    path('', views.index, name='index'),
    path('countries/', countries_list, name='countries_list'),
    
    # Add other URL patterns here
]