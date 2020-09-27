from rest_framework import serializers
from .models import Customers, Assignments


class AssignmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignments
        fields = ('tariffid', 'customerid', 'datefrom', 'dateto', 'invoice', 'tariff_value')
        # depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    kontakty = serializers.StringRelatedField(many=True)
    skupiny = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customers

        fields = (
            'id', 'full_name', 'status', 'kontakty',
            'address', 'zip', 'city',
            'info', 'notes',
            'message', 'deposit',
            'depositdate_asstring', 'sendinvoice', 'modify_event', 'create_event',
            'skupiny', 'balance',
            'is_executed', 'lease_antena', 'lease_iptv', 'block_state'
        )
