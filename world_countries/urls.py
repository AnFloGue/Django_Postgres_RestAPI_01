from django.contrib import admin
from django.urls import path, include
from countries import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('countries/', include('countries.urls')),
    path('api/countries/', views.countries_list),
]