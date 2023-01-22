from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('Id', 'Date_Posted', 'Link', 'Proptype', 'Retailer', 'BHK', 'Locality', 'City', 'Price', 'Carpet_Area', 'Washroom', 'Facing', 'Water_Availability', 'Pantry', 'Price_Sqft', 'Property_Age', 'Parking', 'Description')