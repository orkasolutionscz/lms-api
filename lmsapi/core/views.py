from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from url_filter.integrations.drf import DjangoFilterBackend
from .pagination import CustomLimitPagination


class PrimaryViewSet(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)


class BaseViewSet(PrimaryViewSet):
    """Base viewset for user owned recipe attributes"""
    filter_backends = [DjangoFilterBackend]
    pagination_class = CustomLimitPagination
