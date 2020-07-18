from rest_framework import serializers
from .models import Netdevices


class NetdeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Netdevices
        fields = '__all__'
