from rest_framework import generics
from .models import Company, Location
from .serializers import CompanySerializer, LocationSerializer

# Create your views here.


class LocationList(generics.ListAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer