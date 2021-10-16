from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views

router = DefaultRouter()
router.register('cust_all', views.CustomersViewSet, basename='all')
router.register('cust_blocked', views.CustomerBlockedViewSet, basename='blocked')
router.register('cust_executed', views.CustomerExecutedViewSet, basename='executed')
router.register('cust_assigments', views.AssignmentsViewSet)
router.register('cust_tariffs_all', views.TariffsAllViewSet)


# app_name = 'customers'

urlpatterns = [
    path('/', include(router.urls))
]
