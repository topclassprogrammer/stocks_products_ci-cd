from django.test import TestCase

from logistic.models import Product, Stock


class TestProducts(TestCase):

    def test_product(self):
        new_product = Product.objects.create(title='Капуста',
                                             description='Овощ')
        with self.subTest('Не найден созданный продукт'):
            self.assertIn(new_product, Product.objects.all())
        with self.subTest('Продукт не был удален'):
            removing_product = Product.objects.filter(
                title='Капуста').delete()
            self.assertEqual(removing_product[0], 1)

    def test_stock(self):
        new_stock = Stock.objects.create(address='ул. Тестовая')
        with self.subTest('Не найден созданный склад'):
            self.assertIn(new_stock, Stock.objects.all())
        with self.subTest('Склад не был удален'):
            removing_stock = Stock.objects.filter(
                address='ул. Тестовая').delete()
            self.assertEqual(removing_stock[0], 1)



