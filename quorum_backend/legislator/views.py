from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Legislator
import csv

@api_view(['GET'])
def list_supported_and_opposed_bills(request):
    legislator_query = Legislator.objects.raw("""
        SELECT legislator.id, legislator.name,
        (SELECT COUNT(*) FROM vote_results as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 1) as supported_bills,
        (SELECT COUNT(*) FROM vote_results as vr WHERE vr.legislator_id = legislator.id AND vr.vote_type = 2) as opposed_bills
        FROM legislator
    """)

    result = []
    for obj in legislator_query:
        result.append({
            'legislator': {'id': obj.id, 'name': obj.name},
            'supported_bills': obj.supported_bills,
            'opposed_bills': obj.opposed_bills
        })
    
    return Response(result)

@api_view(['POST'])
def import_csv(request):
    if 'file' not in request.FILES:
        return Response({'message': 'No file uploaded'}, status=400)
    
    csv_file = request.FILES['file'].read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Legislator.objects.create(
            id=row['id'],
            name=row['name']
        )
    return Response({'message': 'Legislator CSV file uploaded successfully'})