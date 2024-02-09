from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from bill.models import Bill
from legislator.models import Legislator
from .models import Vote, Vote_Results
import csv

@api_view(['POST'])
def import_vote_csv(request):
    if 'file' not in request.FILES:
        return Response({'message': 'No file uploaded'}, status=400)
    
    csv_file = request.FILES['file'].read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        bill = Bill.objects.get(id=row['bill_id'])
        Vote.objects.create(
            id=row['id'],
            bill=bill
        )
    return Response({'message': 'Vote CSV file uploaded successfully'})

@api_view(['POST'])
def import_results_csv(request):
    if 'file' not in request.FILES:
        return Response({'message': 'No file uploaded'}, status=400)
    
    csv_file = request.FILES['file'].read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        legislator = Legislator.objects.get(id=row['legislator_id'])
        vote = Vote.objects.get(id=row['vote_id'])
        Vote_Results.objects.create(
            id=row['id'],
            legislator=legislator,
            vote=vote,
            vote_type=row['vote_type']
        )
    return Response({'message': 'Vote Results CSV file uploaded successfully'})