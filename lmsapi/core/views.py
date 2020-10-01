from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from url_filter.integrations.drf import DjangoFilterBackend


class BaseViewSet(viewsets.ModelViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    filter_backends = [DjangoFilterBackend]
