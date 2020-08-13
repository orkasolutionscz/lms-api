from rest_framework import serializers
from .models import Routers


class RoutersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Routers
        fields = ('__all__')
        read_only_fields = ('created', )
