from .models import Entries
from rest_framework import serializers

class EntriesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Entries
        fields=('Id', 'Posted_by', 'PG_for', 'Link', 'Owner', 'Locality', 'City', 'Proptype', 'Charges', 'Description')