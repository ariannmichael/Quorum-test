from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Bill
import csv

@api_view(['GET'])
def list(request):
    bill_query = Bill.objects.raw("""
        SELECT bill.id, bill.title, 
        (SELECT COUNT(*) FROM vote_results as vr LEFT JOIN vote v ON v.id = vr.vote_id  WHERE v.bill_id = bill.id AND vr.vote_type = 1) as supporters, 
        (SELECT COUNT(*) FROM vote_results as vr LEFT JOIN vote v ON v.id = vr.vote_id  WHERE v.bill_id = bill.id AND vr.vote_type = 2) as opposers, bill.primary_sponsor
        FROM bill_bill as bill
    """)

    result = []
    for obj in bill_query:
        result.append({
            'bill': {'id': obj.id, 'title': obj.title},
            'supporters': obj.supporters,
            'opposers': obj.opposers,
            'primary_sponsor': obj.primary_sponsor
        })

    return Response(result)


@api_view(['POST'])
def import_csv(request):
    if 'file' not in request.FILES:
        return Response({'message': 'No file uploaded'}, status=400)
    
    csv_file = request.FILES['file'].read().decode('utf-8').splitlines()
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        Bill.objects.create(
            id=row['id'],
            title=row['title'],
            primary_sponsor=row['sponsor_id']
        )
    return Response({'message': 'Bill CSV file uploaded successfully'})