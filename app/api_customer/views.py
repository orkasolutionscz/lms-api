from rest_framework import permissions, viewsets
from .serializers import CustomerSerializer
from core.models import Customers
lms_block_msg_user = 'Služby Vám byly omezeny z důvodu nesrovnalostí v platbách za minulá období.'


class CustomerBlockedShowAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customers.objects.filter(message=lms_block_msg_user).filter(deleted=0)
