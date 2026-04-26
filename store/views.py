# store/views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Category, Brand, Product, Banner, HappyClient, HomeSection
from .serializers import (
    CategorySerializer, 
    BrandSerializer, 
    ProductSerializer, 
    BannerSerializer,
    HappyClientSerializer,
    HomeSectionSerializer
)

class HappyClientList(generics.ListAPIView):
    queryset = HappyClient.objects.all()
    serializer_class = HappyClientSerializer
    permission_classes = [AllowAny]
    
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [AllowAny]

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    
    # slug দিয়ে ফিল্টার করার জন্য ম্যাজিক লাইন!
    lookup_field = 'slug'

    # ক্যাটাগরি বা ব্র্যান্ড দিয়ে ফিল্টার করার জন্য লজিক
    def get_queryset(self):
        queryset = Product.objects.all()
        category = self.request.query_params.get('category', None)
        brand = self.request.query_params.get('brand', None)
        
        if category is not None:
            queryset = queryset.filter(category__slug=category)
        if brand is not None:
            queryset = queryset.filter(brand__slug=brand)
            
        return queryset

class BannerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Banner.objects.filter(is_active=True)
    serializer_class = BannerSerializer
    permission_classes = [AllowAny]
    
class HomeSectionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HomeSection.objects.filter(is_active=True)
    serializer_class = HomeSectionSerializer
    permission_classes = [AllowAny]