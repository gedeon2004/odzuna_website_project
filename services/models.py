from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.urls import reverse


class Vehicule(models.Model):
    TYPE_CHOICES = [
        ('NEUF', 'Neuf'),
        ('OCCASION', 'Occasion'),
    ]

    TRANSMISSION_CHOICES = [
        ('AUTO', 'Automatique'),
        ('MANUEL', 'Manuelle'),
    ]

    CARBURANT_CHOICES = [
        ('ESSENCE', 'Essence'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIQUE', 'Électrique'),
    ]

    marque = models.CharField(max_length=100, blank=True, null=True)
    modele = models.CharField(max_length=100)
    annee = models.CharField(max_length=4, default="1999")
    prix = models.DecimalField(max_digits=12, decimal_places=0)
    kilometrage = models.PositiveIntegerField(default=0)
    nb_places = models.PositiveIntegerField(default=0)
    couleur = models.CharField(max_length=50, blank=True, null=True)
    photo = models.ImageField(upload_to='vehicules/')
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    carburant = models.CharField(max_length=10, choices=CARBURANT_CHOICES, default='ESSENCE')
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, default='non-defini')
    disponible = models.BooleanField(default=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("services:detail_vehicule", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.marque} {self.modele}"


class PieceDetachee(models.Model):
    reference = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    compatible_avec = models.ManyToManyField('Vehicule', related_name='pieces_compatibles')

    
    photo = models.ImageField(
        upload_to='pieces/',
        blank=True,
        null=True,
        verbose_name="Photo de la pièce"
    )

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


class DemandeAideEmploi(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    telephone = models.CharField(max_length=20, blank=True, null=True)
    domaine = models.CharField(max_length=100)
    besoin = models.TextField()
    date_soumission = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nom} - {self.domaine}"
