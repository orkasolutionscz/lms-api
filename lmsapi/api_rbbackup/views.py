from .models import Routers, RoutersType
from .serializers import RouterSerializer, RouterTypeSerializer
from core.views import BaseViewSet, PrimaryViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework import viewsets

@api_view(['POST'])
def find_router(request):
    routers = Routers.objects.filter(addr=request.data['addr'])
    serializer = RouterSerializer(routers, many=True)
    return Response(serializer.data)


class RouterViewSet(viewsets.ModelViewSet):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer

    @action(detail=True, methods=['POST'])
    def backup_router(self, request, pk=None):
        response = {'message': 'spustil jsem backup routeru'}
        return Response(response, status=status.HTTP_200_OK)


class RouterTypeViewSet(BaseViewSet):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer
