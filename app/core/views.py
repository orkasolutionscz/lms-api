from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter


class BaseLmsApiAttrViewSet(viewsets.ReadOnlyModelViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = ( OrderingFilter, SearchFilter)


