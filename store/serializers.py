from rest_framework import serializers
from .models import (Category, Brand, HappyClient, HomeSection, Product, 
                     ProductImage, Banner, ProductColor, Storage, Region,
                     CustomizationCategory, CustomizationSubCategory, CustomizationOption)

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

# ==========================================
# --- 3-Level Mac Customization Serializers ---
# ==========================================

class CustomizationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomizationOption
        fields = ['id', 'name', 'description', 'extra_price', 'is_default', 'depends_on']

class CustomizationSubCategorySerializer(serializers.ModelSerializer):
    options = CustomizationOptionSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomizationSubCategory
        fields = ['id', 'name', 'description', 'order','depends_on', 'options']

class CustomizationCategorySerializer(serializers.ModelSerializer):
    sub_categories = CustomizationSubCategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomizationCategory
        fields = ['id', 'name', 'order','depends_on', 'sub_categories']

# ==========================================
# --- Product Serializer ---
# ==========================================

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    colors = ProductColorSerializer(many=True, read_only=True) 
    storages = StorageSerializer(many=True, read_only=True) 
    regions = RegionSerializer(many=True, read_only=True) 
    category_name = serializers.ReadOnlyField(source='category.name')
    brand_name = serializers.ReadOnlyField(source='brand.name')
    category_slug = serializers.ReadOnlyField(source='category.slug') # ব্রেডক্রাম্বের জন্য സ্লাগ
    
    # 3-Level Customization Categories যুক্ত করা হলো
    customization_categories = CustomizationCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'category', 'category_name', 'category_slug', 'brand', 'brand_name', 
            'name', 'slug', 'product_code', 'description', 'specifications', 
            'warranty_info', 'price', 'discount_price', 'stock', 
            'delivery_timescale', 'emi_available', 'colors', 'storages', 'regions', 'images', 
            'is_exclusive', 'is_top_deal', 'is_customizable_mac', 'customization_categories', 'created_at'
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