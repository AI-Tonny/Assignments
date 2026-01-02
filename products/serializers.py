from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'user', 'title', 'price', 'description', 'is_available', 'rating', 'photo_url', 'created_at']
        read_only_fields = ['user']