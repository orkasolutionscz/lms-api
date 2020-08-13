from rest_framework import serializers
from .models import LmsUsers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LmsUsers
        fields = ('__all__')
