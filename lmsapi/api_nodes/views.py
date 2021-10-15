from .serializers import NodesSerializer, MacsSerializer, IpHistorySerializer
from .models import Nodes, Macs, BtIphistory
from core.views import BaseViewSet
import core.iptools as iptools
from rest_framework import generics


class NodeViewSet(BaseViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer


class MacsViewSet(BaseViewSet):
    """Manage Nodes in the database"""
    queryset = Macs.objects.all()
    serializer_class = MacsSerializer


class IpHistoryViewSet(generics.ListAPIView):
    """
    Parametry pro vybery:
    ip - format 192.168.1.0 nebo 123456789
    """
    # queryset = BtIphistory.objects.all()
    serializer_class = IpHistorySerializer
    # filter_fields = ['ip', 'cid', 'typ']

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = BtIphistory.objects.all()
        p_ip = self.request.query_params.get('ip', None)
        p_cid = self.request.query_params.get('cid', None)
        if p_ip:
            par_ip = iptools.validIP(p_ip)
            print(f'queryset filter ip={par_ip}')
            queryset = queryset.filter(ip=par_ip).order_by('-datum')
        elif p_cid:
            queryset = queryset.filter(cid=p_cid).order_by('-datum')
        return queryset