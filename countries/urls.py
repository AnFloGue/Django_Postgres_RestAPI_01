from django.urls import path
from .views import countries_list, countries_detail

urlpatterns = [
    path('', countries_list, name='countries_list'),
    path('api/countries', countries_list),
    path('api/countries/<int:pk>', countries_detail)
]

# ----------------------------------------
# from django.urls import path, re_path
# from .views import countries_list
# from countries import views
#
# urlpatterns = [
#     path('', countries_list, name='countries_list'),
#     re_path(r'^api/countries$', views.countries_list),
#     re_path(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_detail)
# ]