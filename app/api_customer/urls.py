from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views


router = DefaultRouter()
router.register('customers', views.CustomerBlockedShowAPIView)

app_name = 'api_customer'

urlpatterns = [
    path('', include(router.urls))
]