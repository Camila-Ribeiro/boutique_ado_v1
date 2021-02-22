from django.test import TestCase
from .models import Product, Category


# Create your tests here.


class TestProductViews(TestCase):

    def test_get_all_products_list(self):
        response = self.client.get('/products', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_object_or_404(self):
        response = self.client.get('/products/200', follow=True)
        # self.assertRedirects(response, '/products/200', status_code=301, target_status_code=301)
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'products/product_detail.html')