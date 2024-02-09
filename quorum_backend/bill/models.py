from django.db import models

# Create your models here.

class Bill(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    primary_sponsor = models.IntegerField()

    def __str__(self):
        return self.title

    class Model:
        db_table = 'bill'