from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NodeViewSet, MacsViewSet, IpHistoryViewSet

router = DefaultRouter()
router.register('Nodes', NodeViewSet, basename='all_nodes')
router.register('Macs', MacsViewSet, basename='all_macs')
router.register('iphistory', IpHistoryViewSet)

app_name = 'netnodes'

urlpatterns = [
    path('', include(router.urls))
]
