from django.db import models
from datetime import date
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Create your models here.
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Liga(models.Model):
    kraj = models.CharField(max_length=64)
    nazwa = models.CharField(max_length=64)
    poziom = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nazwa + ' ( '+ self.kraj +' ) '


class Agent(models.Model):
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko

class Klub(models.Model):
    nazwa = models.CharField(max_length=64)
    miasto = models.CharField(max_length=64)
    rok_zalozenia = models.IntegerField(null=True, blank=True)
    liga = models.ForeignKey(Liga, on_delete=models.CASCADE, blank=True, null=True, related_name='kluby')

    def __str__(self):
        return self.nazwa_klubu()

    def nazwa_klubu(self):
        return self.nazwa

class Piłkarz(models.Model):
    pozycja_rodzaje = {
        ("Tam gdzie trzeba", "Tam gdzie trzeba"),
        ("Bramkarz", "Bramkarz"),
        ("Obrońca", "Obrońca"),
        ("Pomocnik", "Pomocnik"),
        ("Napastnik", "Napastnik"),
    }
    imie = models.CharField(max_length=32)
    nazwisko = models.CharField(max_length=32)
    data_urodzenia = models.DateField(default='2000-01-01')
    pozycja = models.CharField(choices=pozycja_rodzaje, default="Tam gdzie trzeba", max_length=32)
    czy_aktywny = models.BooleanField(default=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, blank=True, null=True)
    klub = models.ForeignKey(Klub, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko



