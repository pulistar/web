
from django.urls import path, include
from rest_framework import routers
from actividades import views 

router = routers.DefaultRouter()
router.register(r'actividades', views.ActividadView, 'actividades')  

urlpatterns = [
    path('', include(router.urls)),
]


