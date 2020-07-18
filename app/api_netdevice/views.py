from .serializers import NetdeviceSerializer
from .models import Netdevices
from core.views import BaseLmsApiAttrViewSet


class DevicesViewSet(BaseLmsApiAttrViewSet):
    """Manage tags in the database"""
    queryset = Netdevices.objects.all()
    serializer_class = NetdeviceSerializer
