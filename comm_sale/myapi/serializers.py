from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('Id', 'Date_Posted', 'Link', 'Owner', 'Carpet_Area', 'Locality', 'City', 'Proptype', 'Washroom', 'Price', 'Price_Sqft', 'Parking', 'Facing', 'Pantry', 'Water_Availability', 'Property_Age', 'Overlooking', 'Description')