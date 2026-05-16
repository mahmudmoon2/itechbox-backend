from rest_framework import serializers
from .models import (Category, Brand, HappyClient, HomeSection, Product, 
                     ProductImage, Banner, ProductColor, Storage, Region,
                     CustomizationCategory, CustomizationOption) # নতুন মডেলগুলো ইমপোর্ট করা হলো

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storage
        fields = ['id', 'name']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']

class ProductColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ['id', 'name', 'hex_code', 'image']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'is_feature']

# --- Mac Customization Serializers ---
class CustomizationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizationOption
        fields = ['id', 'name', 'extra_price', 'is_default']

class CustomizationCategorySerializer(serializers.ModelSerializer):
    options = CustomizationOptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomizationCategory
        fields = ['id', 'name', 'description', 'order', 'options']

# --- Product Serializer ---
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True) 
    storages = StorageSerializer(many=True, read_only=True) 
    regions = RegionSerializer(many=True, read_only=True) 
    category_name = serializers.ReadOnlyField(source='category.name')
    brand_name = serializers.ReadOnlyField(source='brand.name')
    
    # Customization Categories যুক্ত করা হলো
    customization_categories = CustomizationCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'category_name', 'brand', 'brand_name', 
            'name', 'slug', 'product_code', 'description', 'specifications', 
            'warranty_info', 'price', 'discount_price', 'stock', 
            'delivery_timescale', 'emi_available', 'colors', 'storages', 'regions', 'images', 
            'is_exclusive', 'is_top_deal', 'is_customizable_mac', 'customization_categories', 'created_at'
        ] # is_customizable_mac এবং customization_categories যোগ করা হয়েছে

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