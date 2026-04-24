# store/serializers.py
from rest_framework import serializers
from .models import Category, Brand, Product, ProductImage, Banner

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_feature']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    category_name = serializers.ReadOnlyField(source='category.name')
    brand_name = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug', 'description', 'price', 'discount_price', 
            'stock', 'category', 'category_name', 'brand', 'brand_name', 
            'is_exclusive', 'is_top_deal', 'images'
        ]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'