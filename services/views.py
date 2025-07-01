from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Vehicule
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import PieceDetachee
from .models import LessonAutoEcole
from core.models import User, Client
from .forms import DemandeEmploiForm
from .models import DemandeAideEmploi


def automobiles(request):
    type_filter = request.GET.get('type')
    dispo_filter = request.GET.get('dispo')
    search_query = request.GET.get('q')

    vehicules = Vehicule.objects.all()

    if type_filter in ['NEUF', 'OCCASION']:
        vehicules = vehicules.filter(type=type_filter)

    if dispo_filter == '1':
        vehicules = vehicules.filter(disponible=True)
    elif dispo_filter == '0':
        vehicules = vehicules.filter(disponible=False)

    if search_query:
        vehicules = vehicules.filter(modele__icontains=search_query)

    # Paginator
    paginator = Paginator(vehicules, 6)  # 6 véhicules par page
    page = request.GET.get('page')
    vehicules_page = paginator.get_page(page)

    context = {
        'vehicules': vehicules_page,
        'type_filter': type_filter,
        'dispo_filter': dispo_filter,
        'search_query': search_query
    }
    return render(request, 'services/automobiles.html', context)


def ajouter_favori(request, id):
    favoris = request.session.get('favoris', [])
    if str(id) not in favoris:
        favoris.append(str(id))
        request.session['favoris'] = favoris
        return JsonResponse({'status': 'added'})
    else:
        return JsonResponse({'status': 'exists'})

def vehicule_detail(request, pk):
    vehicule = get_object_or_404(Vehicule, pk=pk)
    return render(request, 'services/vehicule_detail.html', {'vehicule': vehicule})


def pieces(request):
    search_query = request.GET.get('q')
    vehicule_id = request.GET.get('vehicule')

    pieces = PieceDetachee.objects.all()

    if search_query:
        pieces = pieces.filter(reference__icontains=search_query)

    if vehicule_id:
        pieces = pieces.filter(compatible_avec__id=vehicule_id)

    vehicules = Vehicule.objects.all()

    context = {
        'pieces': pieces.distinct(),
        'vehicules': vehicules,
        'vehicule_id': vehicule_id,
        'search_query': search_query
    }

    return render(request, 'services/pieces.html', context)

def piece_detail(request, pk):
    piece = get_object_or_404(PieceDetachee, pk=pk)
    return render(request, 'services/piece_detail.html', {'piece': piece})


def permis(request):
    instructeurs = User.objects.all()
    eleves = Client.objects.all()

    instructeur_id = request.GET.get('instructeur')
    eleve_id = request.GET.get('eleve')
    statut = request.GET.get('statut')

    lecons = LessonAutoEcole.objects.all()

    if instructeur_id:
        lecons = lecons.filter(instructeur__id=instructeur_id)

    if eleve_id:
        lecons = lecons.filter(eleve__id=eleve_id)

    if statut:
        lecons = lecons.filter(statut=statut)

    context = {
        'lecons': lecons,
        'instructeurs': instructeurs,
        'eleves': eleves,
        'instructeur_id': instructeur_id,
        'eleve_id': eleve_id,
        'statut': statut,
        'total': LessonAutoEcole.objects.count(),
        'planifiees': LessonAutoEcole.objects.filter(statut='PLANIFIEE').count(),
        'terminees': LessonAutoEcole.objects.filter(statut='TERMINEE').count(),
    }

    return render(request, 'services/permis.html', context)



def consulaires(request):
    services = [
        {
            'titre': 'Légalisation de documents',
            'description': 'Authentification de documents officiels pour usage à l’international.',
            'icone': 'fas fa-stamp'
        },
        {
            'titre': 'Traduction assermentée',
            'description': 'Traductions officielles acceptées par les ambassades et institutions.',
            'icone': 'fas fa-language'
        },
        {
            'titre': 'Casier judiciaire',
            'description': 'Assistance pour obtenir un extrait de casier judiciaire.',
            'icone': 'fas fa-file-signature'
        },
        {
            'titre': 'Assistance visa',
            'description': 'Montage de dossiers de visa et conseils personnalisés.',
            'icone': 'fas fa-passport'
        },
        {
            'titre': 'Lettre d’invitation',
            'description': 'Rédaction et formalisation des lettres d’invitation officielles.',
            'icone': 'fas fa-envelope-open-text'
        },
        {
            'titre': 'Attestation d’hébergement',
            'description': 'Documents nécessaires pour les demandes de visa touristiques.',
            'icone': 'fas fa-home'
        },
    ]
    return render(request, 'services/consulaires.html', {'services': services})



def emploi(request):
    # Bloc des services (grille visuelle)
    services = [
        {
            'titre': 'CV professionnel',
            'description': 'Rédaction ou mise en forme d’un CV moderne adapté aux standards internationaux.',
            'icone': 'fas fa-id-badge'
        },
        {
            'titre': 'Lettre de motivation',
            'description': 'Aide à la rédaction personnalisée en fonction de l’offre ou du secteur.',
            'icone': 'fas fa-file-alt'
        },
        {
            'titre': 'Orientation emploi',
            'description': 'Coaching et conseils sur les secteurs porteurs au Togo et à l’étranger.',
            'icone': 'fas fa-briefcase'
        },
        {
            'titre': 'Préparation entretien',
            'description': 'Simulations d’entretien pour renforcer la confiance et la clarté.',
            'icone': 'fas fa-comments'
        },
        {
            'titre': 'Opportunités à l’international',
            'description': 'Accompagnement sur les procédures de recrutement au Canada, USA, Europe...',
            'icone': 'fas fa-globe-africa'
        },
        {
            'titre': 'Suivi de dossier',
            'description': 'Accompagnement complet de votre candidature jusqu’à l’embauche ou la réponse.',
            'icone': 'fas fa-check-circle'
        }
    ]

    # Traitement du formulaire
    if request.method == 'POST':
        form = DemandeEmploiForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Votre demande a bien été envoyée. Nous vous contacterons sous peu.")
            return redirect('aide_emploi')
    else:
        form = DemandeEmploiForm()

    # Rendu final
    return render(request, 'services/emploi.html', {
        'services': services,
        'form': form
    })

