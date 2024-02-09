from django.urls import path
from . import views

urlpatterns = [
    path('import-csv', views.import_csv, name='import_csv'),
    path('list-bills', views.list_supported_and_opposed_bills, name='list_supported_and_opposed_bills')
]