from django.urls import path
from . import views

app_name = 'travel'

urlpatterns = [
    path('immigration/', views.immigration, name='immigration'),
    path('canada/', views.canada, name='canada'),
    path('schengen/', views.schengen, name='schengen'),
    path('usa/', views.usa, name='usa'),
    path('loterie/', views.loterie, name='loterie'),
]