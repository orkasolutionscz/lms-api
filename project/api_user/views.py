from core.views import BaseLmsApiAttrViewSet
from .models import LmsUsers, UserGroup
from .serializers import UserSerializer, UserGroupSerializer


class UserViewSet(BaseLmsApiAttrViewSet):
    queryset = LmsUsers.objects.all().order_by('name')
    serializer_class = UserSerializer


class UserGroupViewSet(BaseLmsApiAttrViewSet):
    model = UserGroup
    serializer_class = UserGroupSerializer
