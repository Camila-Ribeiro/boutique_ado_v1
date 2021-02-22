from django.test import TestCase


# Create your tests here.


class TestProfileViews(TestCase):

    def test_get_object_or_404(self):
        self.client.login(username='lololo', password='J9j+K5MS')
        response = self.client.get('/profile', follow=True)
        # self.assertRedirects(response, '/products/200', status_code=301, target_status_code=301)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

