from django.urls import path
from .views import *


app_name = 'cajeros'

urlpatterns = [
    path('', home, name='cajero_home'),
]
