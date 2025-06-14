from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('automobiles/', views.automobiles, name='automobiles'),
    path('pieces/', views.pieces, name='pieces'),
    path('permis/', views.permis, name='permis'),
    path('emploi/', views.emploi, name='emploi'),
]