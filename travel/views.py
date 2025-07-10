from django.shortcuts import render
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

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

def reservation(request):
    return render(request, 'travel/reservation.html')

def generate_pdf(request):
    template_path = 'travel/reservation_pdf.html'
    context = {}  # Ajoutez vos données ici
    
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reservation.pdf"'
    
    template = get_template(template_path)
    html = template.render(context)
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Erreur lors de la génération du PDF')
    return response