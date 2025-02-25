from django.test import TestCase
from Restaurant.models import Menu, Booking

class MenuTestCase(TestCase):
    def test_menu(self):
        menu = Menu.objects.create(ID=1, Title='Burger', Price=5.50, Inventory=100)
        self.assertEqual(menu.ID, 1)
        self.assertEqual(menu.Title, 'Burger')
        self.assertEqual(menu.Price, 5.50)
        self.assertEqual(menu.Inventory, 100)
        self.assertEqual(str(menu), 'Burger : 5.50')