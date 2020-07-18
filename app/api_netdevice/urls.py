from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DevicesViewSet


router = DefaultRouter()
router.register('Netdevices', DevicesViewSet, basename='all_devices')


app_name = 'netdevices'

urlpatterns = [
    path('', include(router.urls))
]