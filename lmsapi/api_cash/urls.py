from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CashViewSet, CashViewSetPages

router = DefaultRouter()
router.register('all', CashViewSet, basename='all_cash')
router.register('pages', CashViewSetPages, basename='page_cash')

app_name = 'cash'

urlpatterns = [
    path('', include(router.urls))
]
