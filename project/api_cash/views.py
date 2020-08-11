from core.views import BaseLmsApiAttrViewSet
from .models import Cash
from .serializers import CashSerializer
from core.pagination import CustomLimitPagination


class CashViewSet(BaseLmsApiAttrViewSet):
    """
    - Vybirame jen typ 4 coz jsou platby z Banky
    - Setridime nenovejsim datem na zacatek
    """
    queryset = Cash.objects.all().filter(type=4).order_by('-time')
    serializer_class = CashSerializer
    filter_fields = ['customerid', 'comment', 'value']
    ordering_fields = ['customerid', 'value', 'platba_datum']


class CashViewSetPages(BaseLmsApiAttrViewSet):
    """
    - Vybirame jen typ 4 coz jsou platby z Banky
    - Setridime nenovejsim datem na zacatek
    - Strankovani
    - Hledani customera: cash/pages/?customerid=1
    - hledani cisla uctu: cash/pages/?comment__contains=1643321013/0800
    """
    queryset = Cash.objects.all().filter(type=4).order_by('-time')
    serializer_class = CashSerializer
    filter_fields = ['customerid', 'comment', 'value']
    ordering_fields = ['customerid', 'value', 'time']
    pagination_class = CustomLimitPagination
