from django.urls import path
from . import views

urlpatterns = [
    path('import-csv', views.import_vote_csv, name='import_vote_csv'),
    path('results/import-csv', views.import_results_csv, name='import_results_csv'),
]