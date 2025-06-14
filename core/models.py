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
