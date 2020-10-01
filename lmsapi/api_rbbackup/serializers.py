from rest_framework import serializers
from .models import Routers, RoutersType


class RouterTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutersType
        fields = '__all__'


class RouterSerializer(serializers.ModelSerializer):
    dev_type = RouterTypeSerializer(read_only=True, many=True)

    class Meta:
        model = Routers
        fields = ('__all__')
        read_only_fields = ('created', )
