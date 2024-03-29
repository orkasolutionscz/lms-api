"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .api_router import router



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/backup', include('api_rbbackup.urls')),
    path('api/customers', include('api_customer.urls')),

    # path('routerServices/findRouter/', views.find_router)
]

"""
urlpatterns = [
    path('api/customer/', include('api_customer.urls')),
    path('api/netdevice/', include('api_netdevice.urls')),
    path('api/nodes/', include('api_nodes.urls')),
    path('api/cash/', include('api_cash.urls')),
    path('api/users/', include('api_user.urls')),
    path('api/router', include('api_rbbackup.urls')),

]
"""