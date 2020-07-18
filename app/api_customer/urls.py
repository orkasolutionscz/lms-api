from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer.views import CustomerBlockedShowAPIView


router = DefaultRouter()
router.register('customers', CustomerBlockedShowAPIView)

app_name = 'api_customer'

urlpatterns = [
    path('', include(router.urls))
]