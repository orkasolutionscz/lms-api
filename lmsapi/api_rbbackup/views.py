from api_rbbackup import models
from api_rbbackup import serializers

from core.views import BaseViewSet


class RouterViewSet(BaseViewSet):
    """Manage Router v databazi"""
    queryset = models.Routers.objects.all()
    serializer_class = serializers.RouterSerializer
    filter_fields = ['addr', 'devtype', 'isActivated']
    ordering = ['addr']

    def perform_create(self, serializer):
        """Vytvoreni noveho zaznamu"""
        serializer.save()
        """ Tady dame pak volani na celery task"""

    def get_serializer_class(self):
        """Return appropriate serializer class"""
        if self.action == 'retrieve':
            return serializers.RouterDetailSerializer

        return self.serializer_class


class RouterTypeViewSet(BaseViewSet):
    queryset = models.RoutersType.objects.all()
    serializer_class = serializers.RouterTypeSerializer
