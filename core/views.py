from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from .forms import NewsletterForm
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre message a bien été envoyé. Merci de nous avoir contactés.")
            return redirect('contact')
        else:
            messages.error(request, "Une erreur est survenue. Veuillez vérifier le formulaire.")
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def newsletter_inscription(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Merci pour votre inscription à la newsletter.")
        else:
            messages.error(request, "Une erreur est survenue. Vérifiez vos informations.")
    return redirect(request.META.get('HTTP_REFERER', 'home'))
