# store/serializers.py
from rest_framework import serializers
from .models import Category, Brand, HappyClient, HomeSection, Product, ProductImage, Banner, ProductColor

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

# নতুন কালার সিরিয়ালাইজার
class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['id', 'name', 'hex_code']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_feature']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True) # কালার যুক্ত করা হলো
    category_name = serializers.ReadOnlyField(source='category.name')
    brand_name = serializers.ReadOnlyField(source='brand.name')

    class Meta:
        model = Product
        # নতুন ফিল্ডগুলো (product_code, specifications, warranty_info ইত্যাদি) যোগ করা হলো
        fields = [
            'id', 'category', 'category_name', 'brand', 'brand_name', 
            'name', 'slug', 'product_code', 'description', 'specifications', 
            'warranty_info', 'price', 'discount_price', 'stock', 
            'delivery_timescale', 'emi_available', 'colors', 'images', 
            'is_exclusive', 'is_top_deal', 'created_at'
        ]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
        
class HomeSectionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    
    class Meta:
        model = HomeSection
        fields = ['id', 'title', 'products']
        
class HappyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = HappyClient
        fields = '__all__'