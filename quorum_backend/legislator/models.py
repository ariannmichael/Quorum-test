from django.db import models

# Create your models here.
class Legislator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'legislator'