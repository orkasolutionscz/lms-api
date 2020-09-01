from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views

router = DefaultRouter()
router.register('all', views.CustomersAllShowAPIView, basename='vsichni')
router.register('blocked', views.CustomerBlockedShowAPIView, basename='blocked')
router.register('vymahani', views.CustomerBlockedShowAPIView, basename='is_executed')
router.register('pages', views.CustomersPagesShowAPIView, basename='pages_customers')

app_name = 'customers'

urlpatterns = [
    path('', include(router.urls))
]
