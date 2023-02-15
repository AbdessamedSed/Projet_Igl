from django.test import SimpleTestCase

#from django.urls import path
#from accounts.views import RegisterView


class TestUrls(SimpleTestCase):

    def test_mist_url_is_resolved(self):
        assert 1 == 2