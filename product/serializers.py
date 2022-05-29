from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'name', 'slug', ]
        model = Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'category', 'name', 'slug', 'image', 'available']
        model = Product
