from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RbbackupViewSet

router = DefaultRouter()
router.register('RBBackups', RbbackupViewSet, basename='all_routers')
app_name = 'rbbackup'

urlpatterns = [
    path('', include(router.urls))
]
