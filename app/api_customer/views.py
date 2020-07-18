from .serializers import CustomerSerializer
from .models import Customers
from core.views import BaseLmsApiAttrViewSet

lms_block_msg_user = 'Služby Vám byly omezeny z důvodu nesrovnalostí v platbách za minulá období.'


class CustomersAllShowAPIView(BaseLmsApiAttrViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.filter(deleted=0).order_by('id')


class CustomerBlockedShowAPIView(BaseLmsApiAttrViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.filter(message=lms_block_msg_user).filter(deleted=0).order_by('id')
