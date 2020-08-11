from .serializers import NodesSerializer
from .models import Nodes
from core.views import BaseLmsApiAttrViewSet


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer
