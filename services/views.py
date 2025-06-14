from django.shortcuts import render

def automobiles(request):
    return render(request, 'services/automobiles.html')

def pieces(request):
    return render(request, 'services/pieces.html')

def permis(request):
    return render(request, 'services/permis.html')

def emploi(request):
    return render(request, 'services/emploi.html')