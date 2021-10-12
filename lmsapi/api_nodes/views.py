from .serializers import NodesSerializer, MacsSerializer, IpHistorySerializer
from .models import Nodes, Macs, BtIphistory
from core.views import BaseViewSet
import core.iptools as iptools


class NodeViewSet(BaseViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer


class MacsViewSet(BaseViewSet):
    """Manage Nodes in the database"""
    queryset = Macs.objects.all()
    serializer_class = MacsSerializer


class IpHistoryViewSet(BaseViewSet):
    """
    Parametry pro vybery:
    ip - format 192.168.1.0 nebo 123456789
    """
    queryset = BtIphistory.objects.all()
    serializer_class = IpHistorySerializer
    filter_fields = ['ip',]

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BtIphistory.objects.order_by('-datum')
        ip = self.request.query_params.get('ip', None)
        if ip:
            ip = iptools.validIP(ip)

        if ip is not None:
            queryset = queryset.filter(ip=ip)

        return queryset
