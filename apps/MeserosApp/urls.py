from django.urls import path
from .views import *


app_name = 'meseros'

urlpatterns = [
    path('', meseroIndex, name='mesero_home'),
]
