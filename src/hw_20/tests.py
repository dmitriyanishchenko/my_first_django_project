from django.test import TestCase


class TestCarViews(TestCase):
    def test_home(self):
        result = self.client.get('/hw_20/')
        self.assertEqual(result.status_code, 200)
# Create your tests here.
