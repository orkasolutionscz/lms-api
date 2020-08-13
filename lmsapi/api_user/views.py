from core.views import BaseLmsApiAttrViewSet
from .models import LmsUsers
from .serializers import UserSerializer


class UserViewSet(BaseLmsApiAttrViewSet):
    queryset = LmsUsers.objects.all().order_by('name')
    serializer_class = UserSerializer
