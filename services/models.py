from django.db import models

class Voiture(models.Model):
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    annee = models.PositiveIntegerField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='voitures/')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"
