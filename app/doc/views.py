from rest_framework import permissions, viewsets
from .serializers import CustomersSerializer, CustomerGroupSerializer
from .models import Customers, Customergroups
lms_block_msg_user = 'Služby Vám byly omezeny z důvodu nesrovnalostí v platbách za minulá období.'


class CustomersBlockedShowAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomersSerializer
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Customers.objects.filter(message=lms_block_msg_user).filter(deleted=0)


class CustomersShowAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomersSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Customers.objects.filter(deleted=0).order_by('id')
        custid = self.request.query_params.get('id', None)
        custname = self.request.query_params.get('name', None)
        blocked = self.request.query_params.get('blokovani', None)
        if custid is not None:
            queryset = queryset.filter(id=custid)
        elif custname is not None:
            queryset = queryset.filter(lastname=custname)
        elif blocked is not None:
            queryset = queryset.filter(message__isnull=False)

        return queryset


class CustomerGroupsShowAPIView(viewsets.ReadOnlyModelViewSet):
    serializer_class = CustomerGroupSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Customergroups.objects.order_by('id')
        return queryset
