from core.views import BaseViewSet
from .models import LmsUsers
from .serializers import UserSerializer


class UserViewSet(BaseViewSet):
    queryset = LmsUsers.objects.all().order_by('name')
    serializer_class = UserSerializer
