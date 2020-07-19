from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class BaseLmsApiAttrViewSet(viewsets.ReadOnlyModelViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)


