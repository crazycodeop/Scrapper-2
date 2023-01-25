from django.db import models

# Create your models here.
class Entries(models.Model):
    Id=models.IntegerField(primary_key=True)
    Date_Posted=models.TextField()
    Proptype=models.TextField()
    Link=models.TextField()
    Owner=models.TextField()
    Locality=models.TextField()
    City=models.TextField()
    Price=models.TextField()
    Carpet_Area=models.TextField()
    Parking=models.TextField()
    Property_Age=models.TextField()
    Facing=models.TextField()
    Water_Availability=models.TextField()
    Pantry=models.TextField()
    Overlooking=models.TextField()
    Description=models.TextField()

    def __str__(self):
        return self.Owner
