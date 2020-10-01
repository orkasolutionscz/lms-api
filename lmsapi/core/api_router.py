from rest_framework.routers import DefaultRouter
from api_rbbackup.views import RouterViewSet, RouterTypeViewSet
from api_user.views import UserViewSet


router = DefaultRouter()
# Router Backup Devices
router.register('routers', RouterViewSet)
router.register('routers_type', RouterTypeViewSet)
# LMS Useri
router.register('lmsusers', UserViewSet)
