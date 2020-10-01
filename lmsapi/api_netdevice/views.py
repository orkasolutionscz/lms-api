from .serializers import NetdeviceSerializer
from .models import Netdevices
from core.views import BaseViewSet


class DevicesViewSet(BaseViewSet):
    """Manage tags in the database"""
    queryset = Netdevices.objects.all()
    serializer_class = NetdeviceSerializer

