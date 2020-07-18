from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_customer import views


router = DefaultRouter()
router.register('vsichni', views.CustomersAllShowAPIView)
router.register('blokovani', views.CustomerBlockedShowAPIView)


app_name = 'customers'

urlpatterns = [
    path('', include(router.urls))
]