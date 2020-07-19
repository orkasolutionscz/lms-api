from .serializers import NodesSerializer
from .models import Nodes
from core.views import BaseLmsApiAttrViewSet


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer

    def get_queryset(self):
        """
        Zakladni filtr
        /Nodes?ownerid=xyz
        Vrati nam seznam pocitacu pro usera s id xyz
        """
        queryset = Nodes.objects.all().order_by('id')
        owner_id = self.request.query_params.get('ownerid', None)
        if owner_id is not None:
            queryset = queryset.filter(ownerid=owner_id)

        return queryset
