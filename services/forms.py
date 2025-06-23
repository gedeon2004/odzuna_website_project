from django import forms
from .models import DemandeAideEmploi

class DemandeEmploiForm(forms.ModelForm):
    class Meta:
        model = DemandeAideEmploi
        fields = ['nom', 'email', 'telephone', 'domaine', 'besoin']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Adresse email'}),
            'telephone': forms.TextInput(attrs={'placeholder': 'Téléphone'}),
            'domaine': forms.TextInput(attrs={'placeholder': 'Domaine recherché'}),
            'besoin': forms.Textarea(attrs={'placeholder': 'Décrivez vos besoins ou votre situation…'}),
        }
