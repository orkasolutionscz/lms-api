from rest_framework import serializers
from core.models import Customers


class CustomerSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name="customer-detail")
    # kontakty = serializers.StringRelatedField(many=True)
    # skupiny = serializers.StringRelatedField(many=True)

    class Meta:
        model = Customers
        # fields = '__all__'

        fields = ('id', 'full_name', 'status', 'url',
                  # 'kontakty',
                  'message',
                  'deposit',
                  'depositdate_asstring',
                  # 'country',
                  'sendinvoice',
                  'modify_event',
                  'create_event',
                  'skupiny',
                  'balance')

