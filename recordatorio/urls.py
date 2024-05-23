from django.urls import path, include
from rest_framework import routers
from recordatorio import views 

router = routers.DefaultRouter()
router.register(r'recordatorio', views.RecordatorioView, 'recordatorio')
urlpatterns = [
    path('', include(router.urls)),
   
]
