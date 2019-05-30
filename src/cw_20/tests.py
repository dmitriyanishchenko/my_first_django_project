from django.test import TestCase

class TestCustomerViews(TestCase):
    def test_home(self):
        result = self.client.get('/cw_20/home/')
        self.assertEqual(result.status_code, 200)


# Create your tests here.
