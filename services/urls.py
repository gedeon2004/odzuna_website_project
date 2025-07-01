from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('automobiles/', views.automobiles, name='automobiles'),
    path('vehicule/<int:pk>/', views.vehicule_detail, name='detail_vehicule'),
    path('favori/<int:id>/', views.ajouter_favori, name='ajouter_favori'),
    path('pieces/', views.pieces, name='pieces'),
    path('pieces/<int:pk>/', views.piece_detail, name='piece_detail'),
    path('permis/', views.permis, name='permis'),
    path('emploi/', views.emploi, name='emploi'),
    path('consulaires/', views.consulaires, name='consulaires'),
    path('emploi/', views.emploi, name='emploi'),

]