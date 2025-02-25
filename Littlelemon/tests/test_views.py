from django.test import TestCase
from Restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

        Menu.objects.create(ID=1, Title='Burger', Price=5.50, Inventory=100)
        Menu.objects.create(ID=2, Title='Pizza', Price=10.00, Inventory=50)

    def test_getall(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['Title'], 'Burger')
        self.assertEqual(response.data[1]['Title'], 'Pizza')