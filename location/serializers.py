from rest_framework import serializers
from .models import Company, Location


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name']
        model = Company


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'company', 'address', 'city', 'state', 'zipcode']
        model = Location
