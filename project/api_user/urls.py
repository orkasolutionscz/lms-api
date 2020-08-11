from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, UserGroupViewSet

router = DefaultRouter()
router.register('useri', UserViewSet, basename='users')
router.register('skupiny', UserGroupViewSet, basename='users_group')

app_name = 'cash'

urlpatterns = [
    path('', include(router.urls))
]
