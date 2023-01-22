from django.db import models

# Create your models here.
class Entries(models.Model):
    Id=models.IntegerField(primary_key=True)
    Posted_by=models.TextField()
    Proptype=models.TextField()
    Link=models.TextField()
    Owner=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Charges=models.TextField()
    PG_for=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner