from rest_framework.routers import DefaultRouter
from api_rbbackup.views import RouterViewSet, RouterTypeViewSet
from api_user.views import UserViewSet
from api_nodes.views import NodeViewSet, MacsViewSet
from api_cash.views import CashViewSet
from api_customer.views import CustomersViewSet, CustomerBlockedViewSet, CustomerExecutedViewSet, AssignmentsViewSet
from api_netdevice.views import DevicesViewSet


router = DefaultRouter()
# Router Backup Devices
router.register('routers', RouterViewSet)
router.register('routers_type', RouterTypeViewSet)
# LMS Useri
router.register('lmsusers', UserViewSet)
router.register('nodes', NodeViewSet)
router.register('nodes_mac', MacsViewSet)
router.register('cash_bank', CashViewSet)
router.register('customers', CustomersViewSet)
router.register('customers_blocked', CustomerBlockedViewSet)
router.register('customers_executed', CustomerExecutedViewSet)
router.register('customers_assigments', AssignmentsViewSet)
router.register('devices', DevicesViewSet)

