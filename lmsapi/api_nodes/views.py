from .serializers import NodesSerializer, MacsSerializer
from .models import Nodes, Macs
from core.views import BaseLmsApiAttrViewSet


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer


class MacsViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Macs.objects.all()
    serializer_class = MacsSerializer
