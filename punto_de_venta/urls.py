from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admino/', admin.site.urls),
    path('', include('apps.MainApp.urls')),
    path('cajeros/', include('apps.CajerosApp.urls')),
    path('meseros/', include('apps.MeserosApp.urls')),
    path('admin/', include('apps.AdminsApp.urls')),
]
