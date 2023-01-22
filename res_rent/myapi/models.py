from django.db import models

# Create your models here.
class Entries(models.Model):

    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Proptype=models.TextField(null=True)
    Link=models.TextField()
    Owner=models.TextField()
    BHK=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Rent=models.TextField()
    Carpet_Area=models.TextField()
    Furnishing=models.TextField()
    Facing=models.TextField()
    Tenant=models.TextField()
    Floor=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner
