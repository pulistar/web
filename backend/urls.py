from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/act/', include('actividades.urls')),  
    path('api/ali/', include('alimentacion.urls')), 
    path('api/rec/', include('recordatorio.urls')), 
]
