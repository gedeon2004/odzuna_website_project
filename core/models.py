from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class User(AbstractUser):
    telephone = models.CharField(max_length=20)

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    adresse = models.TextField()
    date_naissance = models.DateField()

    def __str__(self):
        return f"{self.user.username}"

class AbonneNewsletter(models.Model):
    email = models.EmailField(unique=True)
    consentement = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=200)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} ({self.email}) - {self.sujet}"
