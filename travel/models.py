from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
# ==== Travel ====

class PaysDestination(models.Model):
    nom = models.CharField(max_length=100)
    exigences = models.TextField()

    def __str__(self):
        return self.nom


class DossierVisa(models.Model):
    TYPE_VISA_CHOICES = [
        ('TOURISME', 'Tourisme'),
        ('AFFAIRES', 'Affaires'),
    ]

    STATUT_CHOICES = [
        ('BR', 'Brouillon'),
        ('SO', 'Soumis'),
        ('VA', 'Validé'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_visa = models.CharField(max_length=20, choices=TYPE_VISA_CHOICES)
    statut = models.CharField(max_length=2, choices=STATUT_CHOICES, default='BR')
    documents = models.FileField(upload_to='dossiers/')
    client = models.ForeignKey('core.Client', on_delete=models.CASCADE, related_name='dossiers')
    pays = models.ForeignKey(PaysDestination, on_delete=models.CASCADE, related_name='dossiers')

    def soumettre(self):
        self.statut = 'SO'
        self.save()

    def valider(self):
        self.statut = 'VA'
        self.save()

    def __str__(self):
        return f"Visa {self.type_visa} - {self.client}"


class RendezVousAmbassade(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=100)
    dossier = models.OneToOneField(DossierVisa, on_delete=models.CASCADE, related_name='rendezvous')

    def __str__(self):
        return f"RDV à {self.lieu} pour {self.dossier}"