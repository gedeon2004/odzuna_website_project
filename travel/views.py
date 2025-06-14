from django.shortcuts import render

def immigration(request):
    return render(request, 'travel/immigration.html')

def canada(request):
    return render(request, 'travel/canada.html')

def schengen(request):
    return render(request, 'travel/schengen.html')

def usa(request):
    return render(request, 'travel/usa.html')

def loterie(request):
    return render(request, 'travel/loterie.html')