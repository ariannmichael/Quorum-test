from django.db import models
from bill.models import Bill
from legislator.models import Legislator

# Create your models here.
class Vote(models.Model):
    id = models.IntegerField(primary_key=True)
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    def __str__(self):
        return self.bill
    
    class Meta:
        db_table = 'vote'

class Vote_Results(models.Model):
    id = models.IntegerField(primary_key=True)
    legislator = models.ForeignKey(Legislator, on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    vote_type = models.IntegerField() # 1 for yea, 2 for nay.

    def __str__(self):
        return self.vote_type
    
    class Meta:
        db_table = 'vote_results'