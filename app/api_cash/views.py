from core.views import BaseLmsApiAttrViewSet
from .models import Cash
from .serializers import CashSerializer
from url_filter.integrations.drf import DjangoFilterBackend


class CashViewSet(BaseLmsApiAttrViewSet):
    """
    - Vybirame jen typ 4 coz jsou platby z Banky
    - Setridime nenovejsim datem na zacatek
    """
    queryset = Cash.objects.all().filter(type=4).order_by('-time')
    serializer_class = CashSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['customerid', 'comment', 'value']
