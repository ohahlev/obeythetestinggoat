<<<<<<< HEAD
from django.urls import resolve
from django.test import TestCase
from lists.views import home_page  
from django.http import HttpRequest

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home_page) 

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>To-Do Lists</title>', html)  
        self.assertTrue(html.endswith('</html>'))
=======
from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)
>>>>>>> 655a9041de80d6100e088e83e4540eba1e144575
