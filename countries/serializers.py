from rest_framework import serializers
from countries.models import Country

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'name', 'capital')