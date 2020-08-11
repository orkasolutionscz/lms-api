from rest_framework import serializers
from .models import Netdevices, Hwtypes, Netcontypes, Nmsgroups


class NetContypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Netcontypes
        fields = '__all__'


class HwtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hwtypes
        fields = '__all__'


class NmsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nmsgroups
        fields = '__all__'


class NetdeviceSerializer(serializers.ModelSerializer):
    hw_type = HwtypeSerializer(many=False)
    con_type = NetContypeSerializer(many=False)
    nms_group = NmsGroupSerializer(many=False)

    class Meta:
        model = Netdevices
        fields = '__all__'
