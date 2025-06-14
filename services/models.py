from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Vehicule(models.Model):
    TYPE_CHOICES = [
        ('NEUF', 'Neuf'),
        ('OCCASION', 'Occasion'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    modele = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    photo = models.ImageField(upload_to='vehicules/')
    disponible = models.BooleanField(default=True)

    def get_absolute_url(self):
        return f"/vehicules/{self.id}/"

    def __str__(self):
        return self.modele


class PieceDetachee(models.Model):
    reference = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    compatible_avec = models.ManyToManyField(Vehicule, related_name='pieces_compatibles')

    def __str__(self):
        return self.reference


class LessonAutoEcole(models.Model):
    STATUT_CHOICES = [
        ('PLANIFIEE', 'Planifiée'),
        ('TERMINEE', 'Terminée'),
    ]

    date = models.DateTimeField()
    instructeur = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='lecons_donnee')
    eleve = models.ForeignKey('core.Client', on_delete=models.CASCADE, related_name='lecons')
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

    def __str__(self):
        return f"Leçon de {self.eleve} le {self.date}"
