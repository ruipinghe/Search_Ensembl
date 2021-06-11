from django.urls import path
from . import views

app_name = 'homelink'

urlpatterns = [
    path('', views.search_data, name='search_data'),
    path('get_species_databases/', views.search_result, name='search_result'),
]

