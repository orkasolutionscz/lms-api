from rest_framework import serializers
from .models import Cash


class CashSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cash
        fields = (
            'id'
            , 'value'
            , 'comment'
            , 'customerid'
            , 'platba_datum'
        )
