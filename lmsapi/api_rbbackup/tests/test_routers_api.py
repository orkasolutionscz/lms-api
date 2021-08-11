from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from api_rbbackup.models import RoutersType, Routers, RouterBackups

from api_rbbackup.serializers import RouterTypeSerializer, RouterSerializer

ROUTERS_URL = reverse('backup:router-list')


class PublicRoutersApiTests(TestCase):
    """Testovani zda je API pro Routers dostupne"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test jestli je nutny login pro nacteni Routers"""
        res = self.client.get(ROUTERS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


# class PrivateRoutersApiTests(TestCase):
#     """Test pro autoriyovaneho usera"""
#
#     def setUp(self):
