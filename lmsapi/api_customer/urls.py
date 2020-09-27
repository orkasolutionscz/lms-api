from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views

router = DefaultRouter()
router.register('all', views.CustomersAllShowAPIView, basename='vsichni')
router.register('blocked', views.CustomerBlockedShowAPIView, basename='blocked')
router.register('vymahani', views.CustomerExecutedShowAPIView, basename='is_executed')
router.register('dluhy', views.CustomerExecutedShowAPIView, basename='dluhy')
router.register('pages', views.CustomersPagesShowAPIView, basename='pages_customers')
router.register('assigments', views.AssignmentsPagesShowAPIView, basename='pages_assigments')

app_name = 'customers'

urlpatterns = [
    path('', include(router.urls))
]
