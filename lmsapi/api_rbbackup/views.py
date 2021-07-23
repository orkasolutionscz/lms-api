from .models import Routers, RoutersType
from .serializers import RouterSerializer, RouterTypeSerializer
from core.views import BaseViewSet, PrimaryViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def find_router(request):
    routers = Routers.objects.filter(addr=request.data['addr'])
    serializer = RouterSerializer(routers, many=True)
    return Response(serializer.data)


class RouterViewSet(PrimaryViewSet):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer


class RouterTypeViewSet(BaseViewSet):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer
