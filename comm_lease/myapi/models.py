from django.db import models

# Create your models here.
class Entries(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField(null=True)
    Proptype=models.TextField(null=True)
    Link=models.TextField()
    Retailer=models.TextField()
    BHK=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Price=models.TextField()
    Carpet_Area=models.TextField()
    Washroom=models.TextField()
    Facing=models.TextField()
    Pantry=models.TextField()
    Parking=models.TextField()
    Water_Availability=models.TextField()
    Price_Sqft=models.TextField()
    Property_Age=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner
