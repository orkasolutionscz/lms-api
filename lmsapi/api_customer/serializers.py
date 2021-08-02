from rest_framework import serializers
from .models import Customers, Customercontacts, Customergroups, Assignments, Tariffs
from api_nodes.serializers import NodesSerializer


class AssignmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignments
        exclude = ['liabilityid', 'period', 'numberplanid']


class TariffsSerializer(serializers.ModelSerializer):
    tariffs = AssignmentsSerializer(read_only=True, many=True )

    class Meta:
        model = Tariffs
        fields = ('name', 'type', 'value', 'tariffs')


class CustomerContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customercontacts
        fields = ('name', 'phone')


class CustomerGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customergroups
        fields = ('name', 'description')


class CustomerSerializer(serializers.ModelSerializer):
    assigments = AssignmentsSerializer(read_only=True, many=True)
    kontakty = CustomerContactSerializer(read_only=True, many=True)
    cust_skupiny = CustomerGroupSerializer(read_only=True, many=True)
    cele_jmeno = serializers.CharField(source="full_name")
    cust_finance = serializers.DecimalField(source="balance", max_digits=10, decimal_places=0)
    mod_info  = serializers.CharField(source="modify_event")
    crea_info = serializers.CharField(source="create_event")
    cust_nodes = NodesSerializer(read_only=True, many=True)

    class Meta:
        model = Customers
        # fields = '__all__'
        exclude = ['divisionid', 'cutoffstop', 'paytime', 'paytype', 'creationdate',
                   'creatorid', 'moddate', 'modid']


class CustomersSerializer(serializers.ModelSerializer):
    kontakty = CustomerContactSerializer(read_only=True, many=True)
    cust_skupiny = CustomerGroupSerializer(read_only=True, many=True)
    cele_jmeno = serializers.CharField(source="full_name")
    cust_finance = serializers.DecimalField(source="balance", max_digits=10, decimal_places=0)
    mod_info = serializers.CharField(source="modify_event")
    crea_info = serializers.CharField(source="create_event")

    class Meta:
        model = Customers
        # fields = '__all__'
        exclude = ['divisionid', 'cutoffstop', 'paytime', 'paytype', 'creationdate',
                   'creatorid', 'moddate', 'modid']
