from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CashViewSet


router = DefaultRouter()
router.register('Cash', CashViewSet, basename='all_cash')


app_name = 'cash'

urlpatterns = [
    path('', include(router.urls))
]