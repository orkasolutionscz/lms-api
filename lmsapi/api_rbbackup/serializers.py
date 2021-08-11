from rest_framework import serializers
from .models import Routers, RoutersType, RouterBackups


class RouterTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoutersType
        fields = ('id', 'type')
        read_only_fields = ('id',)


class RouterBackupSerializer(serializers.ModelSerializer):

    class Meta:
        model = RouterBackups
        fields = '__all__'
        read_only_fields = ('id',)


class RouterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routers
        fields = '__all__'
        read_only_fields = ('id', 'created', )


class RouterDetailSerializer(RouterSerializer):
    """Serialize a recipe detail"""
    router_type = RouterTypeSerializer(read_only=True, many=False)
    router_backups = RouterBackupSerializer(read_only=True, many=True)
