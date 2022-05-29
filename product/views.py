from rest_framework import generics

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



