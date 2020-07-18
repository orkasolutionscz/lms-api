from .serializers import NodesSerializer
from .models import Nodes
from core.views import BaseLmsApiAttrViewSet


class NodeViewSet(BaseLmsApiAttrViewSet):
    """Manage tags in the database"""
    queryset = Nodes.objects.all()
    serializer_class = NodesSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Nodes.objects.all().order_by('id')
        owner_id = self.request.query_params.get('ownerid', None)
        if owner_id is not None:
            queryset = queryset.filter(ownerid=owner_id)

        return queryset
