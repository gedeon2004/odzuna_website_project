from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Vehicule
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import PieceDetachee
from .models import LessonAutoEcole
from core.models import User, Client

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

def vehicule_detail(request, id):
    vehicule = get_object_or_404(Vehicule, id=id)
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

def emploi(request):
    return render(request, 'services/emploi.html')

