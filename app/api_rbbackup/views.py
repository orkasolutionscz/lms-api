from .models import Routers
from .serializers import RoutersSerializer
from core.views import BaseLmsApiAttrViewSet


class RbbackupViewSet(BaseLmsApiAttrViewSet):
    queryset = Routers.objects.all().order_by('addr')
    serializer_class = RoutersSerializer
    ordering_fields = ('addr', 'identity', 'created')
