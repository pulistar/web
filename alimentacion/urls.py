from django.urls import path, include
from rest_framework import routers
from alimentacion import views 

router = routers.DefaultRouter()
router.register(r'alimentacion', views.AlimentacionView, 'alimentacion')  

urlpatterns = [
    path('', include(router.urls)),
   
]
