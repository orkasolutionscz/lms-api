from .models import Routers, RoutersType
from .serializers import RouterSerializer, RouterTypeSerializer
from core.views import BaseViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def find_router(request):
    routers = Routers.objects.filter(addr=request.data['addr'])
    serializer = RouterSerializer(routers, many=True)
    return Response(serializer.data)


class RouterViewSet(BaseViewSet):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer
    filter_fields = ['addr', 'devtype', 'isActivated']


class RouterTypeViewSet(BaseViewSet):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer
