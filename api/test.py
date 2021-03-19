from django.test import TestCase
from django.urls import reverse, resolve
from .models import Piłkarz

class ApiTests(TestCase):

    def test_pierwszy(self):
        assert 1==1

    def test_piłkarz_jako_text(self):
        piłkarz = Piłkarz.objects.create(imie="Andrzej", nazwisko="Piaseczny")
        self.assertEqual(str(piłkarz), "Andrzej Piaseczny")