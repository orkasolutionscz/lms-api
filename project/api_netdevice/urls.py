from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DevicesViewSet, DevicesPagesViewSet


router = DefaultRouter()
router.register('all', DevicesViewSet, basename='all_devices')
router.register('pages', DevicesPagesViewSet, basename='pages_devices')


app_name = 'netdevices'

urlpatterns = [
    path('', include(router.urls))
]