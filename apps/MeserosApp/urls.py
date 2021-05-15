from django.urls import path
from .views import *


app_name = 'meseros'

urlpatterns = [
    path('', home, name='mesero_home'),
]
