from django import forms
from .models import AbonneNewsletter
from .models import ContactMessage

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = AbonneNewsletter
        fields = ['email', 'consentement']
        labels = {
            'consentement': "J'accepte de recevoir des communications par email"
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'sujet', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Votre email'}),
            'sujet': forms.TextInput(attrs={'placeholder': 'Sujet'}),
            'message': forms.Textarea(attrs={'placeholder': 'Votre message...'}),
        }