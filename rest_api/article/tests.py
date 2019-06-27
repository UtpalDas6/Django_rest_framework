from django.test import TestCase
from rest_framework.test import RequestsClient
from .models import Article,Author
# Create your tests here.
class AuthorArticleTestCase(TestCase):
    '''Unit test the Author and Article Models'''
    def setUp(self):
        self.au=Author.objects.create(name='U1',email='unix.roxx@gmail.com')
        self.ar=Article.objects.create(title='Wings of Fire',description='Fire is the eater of evil',body='Fire body,Fire Soul',author=Author.objects.get(name='U1'))
    def testemail(self):
        "Email Unit Tested"
        self.au=Author.objects.get(name='U1')
        self.assertEqual(self.au.email,'unix.roxx@gmail.com')
    def testtitle(self):
        self.ar=Article.objects.get(author=self.au)
        self.assertEqual(self.ar.title,'Wings of Fire')
    def testdescription(self):
        self.assertEqual(self.ar.description,'Fire is the eater of evil')
    def testbody(self):
        self.assertEqual(self.ar.body,'Fire body,Fire Soul')
    def deleteobjects(self):
        Author.objects.delete(name='U1')
        Article.objects.delete(author=Author.objects.get(name='U'))

class ApiTest(TestCase):
    '''Unit Testing for URL End Points'''
    def setUp(self):
        self.client = RequestsClient()
        self.response1 = self.client.get('http://localhost/api/articles/')
        self.response2 = self.client.get('http://localhost/api/authors/')
    def testResponseCode(self):
        assert self.response1.status_code == self.response2.status_code == 200
    def testArtilceResponse(self):
        assert True
    def testAuthorResponse(self):
        assert True

