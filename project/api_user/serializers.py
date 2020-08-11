from rest_framework import serializers
from .models import LmsUsers, UserGroup


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUsers
        fields = ('__all__')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserGroup
        fields = ('__all__')
