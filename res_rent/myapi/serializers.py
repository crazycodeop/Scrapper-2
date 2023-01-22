from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('Id', 'Date_Posted', 'Link', 'Proptype', 'Owner', 'BHK', 'Locality', 'City', 'Rent', 'Carpet_Area', 'Furnishing', 'Facing', 'Tenant', 'Floor', 'Description')