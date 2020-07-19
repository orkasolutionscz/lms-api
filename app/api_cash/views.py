from core.views import BaseLmsApiAttrViewSet
from .models import Cash
from .serializers import CashSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CashViewSet(BaseLmsApiAttrViewSet):
    """Manage Nodes in the database"""
    queryset = Cash.objects.all()
    serializer_class = CashSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['customerid', 'comment', 'value']
