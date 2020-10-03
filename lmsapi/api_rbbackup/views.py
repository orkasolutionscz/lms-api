from .models import Routers, RoutersType
from .serializers import RouterSerializer, RouterTypeSerializer
from core.views import BaseViewSet


class RouterViewSet(BaseViewSet):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer
    filter_fields = ['addr', 'devtype', 'isActivated']


class RouterTypeViewSet(BaseViewSet):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer

