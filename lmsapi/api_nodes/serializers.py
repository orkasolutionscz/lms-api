from rest_framework import serializers
from .models import Nodes, Macs, BtIphistory


class NodesSerializer(serializers.ModelSerializer):
    nodesmacs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Nodes
        fields = '__all__'


class MacsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Macs
        fields = '__all__'


class IpHistorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="iphistory-detail")

    class Meta:
        model = BtIphistory
        fields = ('id', 'ip', 'url', 'iptext', 'cid', 'typ', 'uzivatel', 'datum')
