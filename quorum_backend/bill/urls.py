from django.urls import path
from . import views

urlpatterns = [
    path('import-csv', views.import_csv, name='import_csv'),
    path('list', views.list, name='list')
]