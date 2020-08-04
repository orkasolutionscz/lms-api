from .serializers import NetdeviceSerializer
from .models import Netdevices
from core.views import BaseLmsApiAttrViewSet
from core.pagination import CustomLimitPagination


class DevicesViewSet(BaseLmsApiAttrViewSet):
    """Manage tags in the database"""
    queryset = Netdevices.objects.all()
    serializer_class = NetdeviceSerializer
    filter_fields = ['id', 'name', 'model', 'ports', 'hw_type', 'nms_group', 'con_type']
    ordering_fields = ['id', 'name', 'model', 'ports', 'hw_type', 'nms_group', 'con_type']


class DevicesPagesViewSet(DevicesViewSet):
    pagination_class = CustomLimitPagination
