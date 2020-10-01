from rest_framework import serializers
from .models import Customers, Customercontacts, Customergroups, Assignments, Tariffs


class AssignmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignments
        fields = '__all__'


class TariffsSerializer(serializers.ModelSerializer):

    tariffs = AssignmentsSerializer(read_only=True, many=True)

    class Meta:
        model = Tariffs
        fields = '__all__'


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

    class Meta:
        model = Customers
        fields = '__all__'
