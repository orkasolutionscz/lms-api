from rest_framework import serializers
from .models import Routers


class RoutersSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="smsgw-detail")

    class Meta:
        model = Routers
        fields = ('__all__')
        read_only_fields = ('created',)


