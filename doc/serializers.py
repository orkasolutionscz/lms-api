from rest_framework import serializers
from .models import Customers, Countries, Customergroups


class CountrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False, allow_blank=True, read_only=True)

    class Meta:
        model = Countries
        fields = [
            'name',
        ]


class CustomersSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="customer-detail")
    country = CountrySerializer(read_only=True)
    kontakty = serializers.StringRelatedField(many=True)
    skupiny = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customers
        # fields = '__all__'

        fields = ('id', 'full_name', 'status', 'url',
                  'kontakty',
                  'message',
                  'deposit', 'depositdate_asstring',
                  'country', 'sendinvoice',
                  'modify_event', 'create_event',
                  'skupiny', 'balance')


class CustomerGroupSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="customergroup-detail")

    class Meta:
        model = Customergroups
        fields = ('id', 'url', 'name', 'description', 'members' )
