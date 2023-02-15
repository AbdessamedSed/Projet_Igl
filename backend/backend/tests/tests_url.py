from django.test import SimpleTestCase
from django.shortcuts import reverse

class TestUrls(SimpleTestCase):


    def test_home_status_code(self):
        response = self.client.get('mesannonces/')
        self.assertEquals(response.status_code, 200)