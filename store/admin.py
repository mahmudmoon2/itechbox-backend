# store/admin.py
from django.contrib import admin
from .models import Category, Brand, Product, ProductImage, Banner, Order, OrderItem

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1 # ডিফল্টভাবে একটা এক্সট্রা ইমেজ আপলোড করার ফিল্ড দেখাবে

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'quantity', 'price']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'stock', 'is_top_deal', 'is_exclusive')
    list_filter = ('brand', 'category', 'is_top_deal', 'is_exclusive')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline] # প্রোডাক্ট পেজেই ছবি অ্যাড করার অপশন

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_filter = ('is_active',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'full_name', 'total_price', 'created_at')
    search_fields = ('order_id', 'full_name', 'address')
    readonly_fields = ('order_id', 'user', 'full_name', 'address', 'total_price')
    inlines = [OrderItemInline]