from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'title', 'price', 'product_image', 'product_review', 'product']
        depth = 1
    
    product_id = serializers.IntegerField(write_only=True)