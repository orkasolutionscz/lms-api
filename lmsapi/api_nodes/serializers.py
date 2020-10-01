from rest_framework import serializers
from .models import Nodes, Macs


class NodesSerializer(serializers.ModelSerializer):
    nodesmacs = serializers.StringRelatedField(many=True)

    class Meta:
        model = Nodes
        fields = '__all__'


class MacsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Macs
        fields = '__all__'
