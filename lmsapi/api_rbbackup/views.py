from .models import Routers, RoutersType
from .serializers import RouterSerializer, RouterTypeSerializer
# from core.views import BaseLmsApiAttrViewSet
from rest_framework import generics


class RouterListView(generics.ListCreateAPIView):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer


class RouterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routers.objects.all()
    serializer_class = RouterSerializer


class RouterTypeListView(generics.ListCreateAPIView):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer


class RouterTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoutersType.objects.all()
    serializer_class = RouterTypeSerializer

"""

class RbbackupViewSet(BaseLmsApiAttrViewSet):
    queryset = Routers.objects.all().order_by('addr')
    serializer_class = RoutersSerializer
    ordering_fields = ('addr', 'identity', 'created')

"""