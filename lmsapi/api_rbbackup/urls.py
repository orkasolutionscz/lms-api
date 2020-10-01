from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api_rbbackup import views

# router = DefaultRouter()
# router.register('mk', RbbackupViewSet, basename='mk_routers')
# app_name = 'rbbackup'

urlpatterns = [
    path('router/', views.RouterListView.as_view()),
    path('router/<int:pk>', views.RouterDetailView.as_view()),
    path('routertype/', views.RouterTypeListView.as_view()),
    path('routertype/<int:pk>', views.RouterTypeDetailView.as_view()),

]
