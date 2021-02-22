from django.test import TestCase
from .models import Product, Category
from model_bakery import baker


class TestCategoryModel(TestCase):

    def test_friendly_name_blank_to_true(self):
        # category_name = Category.objects.create(name='Test Model Category Name')
        category_friendly_name = Category.objects.create(friendly_name='Test Model Category Friendly Name')
        # self.assertFalse(category_name.name)
        self.assertTrue(category_friendly_name.friendly_name)

    def test_category_string_method_returns_name(self):
        category_name = Category.objects.create(name='Test Name')
        self.assertEqual(str(category_name), 'Test Name')

    def test_category_string_method_returns_friendly_name(self):
        category_name = Category.objects.create(name='Test Name')
        category_friendly_name = Category.objects.create(name='Test Friendly Name')
        self.assertNotEqual(str(category_name), str(category_friendly_name), 'Test Friendly Name')

    def test_category_string_method_returns_friendly_name(self):
        category_friendly_name = Category.objects.create(name='Test Friendly Name')
        self.assertEqual(str(str(category_friendly_name)), 'Test Friendly Name')
        

    
        
# class TestProductModel(TestCase):
#     def test_product_string_method_returns_name(self):
#         product = Product.objects.create(name='Test Name')
#         self.assertEqual(str(product), 'Test Name')

    # def setUp(self):
    #     product = baker.make('Product')
    #     self.product = baker.make(products.Product)