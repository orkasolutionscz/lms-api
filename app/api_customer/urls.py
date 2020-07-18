from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views


router = DefaultRouter()
router.register('vsichni', views.CustomersAllShowAPIView, basename='all')
router.register('blocked', views.CustomerBlockedShowAPIView, basename='blocked')


app_name = 'customers'

urlpatterns = [
    path('', include(router.urls))
]