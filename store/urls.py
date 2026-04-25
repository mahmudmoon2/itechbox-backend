# store/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BrandViewSet, HomeSectionViewSet, ProductViewSet, BannerViewSet
from .views import HappyClientList
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'banners', BannerViewSet)
router.register(r'home-sections', HomeSectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('clients/', HappyClientList.as_view(), name='client-list'),
]