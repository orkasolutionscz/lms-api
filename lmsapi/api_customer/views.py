from .serializers import CustomerSerializer, AssignmentsSerializer, TariffsSerializer
from .models import Customers, Assignments, Tariffs
from core.views import BaseViewSet

lms_block_msg_user = 'Služby Vám byly omezeny z důvodu nesrovnalostí v platbách za minulá období.'


class CustomersViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.filter(deleted=0).order_by('id')


class CustomerBlockedViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.filter(message=lms_block_msg_user).filter(deleted=0).filter(is_executed=0).order_by('id')


class CustomerExecutedViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.filter(is_executed=1).filter(deleted=0).order_by('id')


"""
class CustomerDluhyViewSet(BaseViewSet):
    serializer_class = CustomerSerializer
    queryset = Customers.objects.raw('select * from customers where is_executed=0 and deleted=0 and balance < 0')
"""


class AssignmentsViewSet(BaseViewSet):
    serializer_class = AssignmentsSerializer
    queryset = Assignments.objects.all()


class TariffsAllViewSet(BaseViewSet):
    serializer_class = TariffsSerializer
    queryset = Tariffs.objects.all()

