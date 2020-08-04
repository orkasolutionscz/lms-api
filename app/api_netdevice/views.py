from .serializers import NetdeviceSerializer
from .models import Netdevices
from core.views import BaseLmsApiAttrViewSet


class DevicesViewSet(BaseLmsApiAttrViewSet):
    """Manage tags in the database"""
    queryset = Netdevices.objects.all()
    serializer_class = NetdeviceSerializer

    def get_queryset(self):
        """
        Zakladni filtr
        /?nms_group=xyz
        Vrati nam seznam netdevices pro nms_group xyz
        """
        queryset = Netdevices.objects.all().order_by('id')
        nms_group_id = self.request.query_params.get('nms_group', None)
        if nms_group_id is not None:
            queryset = queryset.filter(nms_group=nms_group_id)

        return queryset

