from .serializers import NodesSerializer
from .models import Nodes
from core.views import BaseLmsApiAttrViewSet


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage tags in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer
