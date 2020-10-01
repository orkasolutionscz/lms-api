from core.views import BaseViewSet
from .models import Cash
from .serializers import CashSerializer


class CashViewSet(BaseViewSet):
    """
    - Vybirame jen typ 4 coz jsou platby z Banky
    - Setridime nenovejsim datem na zacatek
    """
    queryset = Cash.objects.all().filter(type=4).order_by('-time')
    serializer_class = CashSerializer
    filter_fields = ['comment', 'userid']
