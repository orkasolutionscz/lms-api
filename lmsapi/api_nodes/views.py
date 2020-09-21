from .serializers import NodesSerializer, MacsSerializer
from .models import Nodes, Macs
from core.views import BaseLmsApiAttrViewSet
from core.pagination import CustomLimitPagination


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all().order_by('ownerid')
    serializer_class = NodesSerializer
    pagination_class = CustomLimitPagination
    filter_fields = ['ownerid']


class MacsViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Macs.objects.all()
    serializer_class = MacsSerializer
    pagination_class = CustomLimitPagination
