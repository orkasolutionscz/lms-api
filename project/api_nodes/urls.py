from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import NodeViewSet

router = DefaultRouter()
router.register('Nodes', NodeViewSet, basename='all_nodes')

app_name = 'netnodes'

urlpatterns = [
    path('', include(router.urls))
]
