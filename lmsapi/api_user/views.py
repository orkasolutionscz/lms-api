from core.views import PrimaryViewSet
from .models import LmsUsers
from .serializers import UserSerializer


class UserViewSet(PrimaryViewSet):
    queryset = LmsUsers.objects.all().order_by('name')
    serializer_class = UserSerializer
