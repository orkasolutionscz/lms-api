from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_rbbackup import views

router = DefaultRouter()
router.register('routers', views.RouterViewSet)
router.register('routers_type', views.RouterTypeViewSet)

# app_name = 'backups'

urlpatterns = [
    path('/', include(router.urls))
]
