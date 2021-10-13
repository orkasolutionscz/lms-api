from rest_framework import serializers
from .models import Nodes, Macs, BtIphistory


class MacsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Macs
        fields = '__all__'


class NodesSerializer(serializers.ModelSerializer):
    nodesmacs = MacsSerializer(read_only=True, many=True)

    class Meta:
        model = Nodes
        fields = '__all__'


class IpHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BtIphistory
        fields = '__all__'
