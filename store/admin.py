from django.contrib import admin
from .models import (
    Category, Brand, Product, ProductImage, Banner, 
    Order, OrderItem, HomeSection, HappyClient, ProductColor, Storage, Region
)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

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

@admin.register(ProductColor)
class ProductColorAdmin(admin.ModelAdmin):
    list_display = ('name', 'hex_code')
    search_fields = ('name',)

# --- নতুন স্টোরেজ এবং রিজিয়ন অ্যাডমিন ---
@admin.register(Storage)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_code', 'brand', 'price', 'stock', 'is_top_deal', 'emi_available')
    list_filter = ('brand', 'category', 'is_top_deal', 'is_exclusive', 'emi_available')
    search_fields = ('name', 'product_code', 'description')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline]
    
    # স্টোরেজ এবং রিজিয়ন অ্যাড করা হলো
    filter_horizontal = ('colors', 'storages', 'regions')

    fieldsets = (
        ('Basic Information', {
            'fields': ('category', 'brand', 'name', 'slug', 'product_code')
        }),
        ('Descriptions & Specs (HTML)', {
            'fields': ('description', 'specifications', 'warranty_info'),
            'classes': ('collapse',), 
        }),
        ('Pricing & Stock', {
            'fields': ('price', 'discount_price', 'stock')
        }),
        ('Attributes & Delivery', {
            'fields': ('colors', 'storages', 'regions', 'delivery_timescale', 'emi_available')
        }),
        ('UI Display Flags', {
            'fields': ('is_exclusive', 'is_top_deal')
        }),
    )

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'placement', 'is_active') 
    list_filter = ('placement', 'is_active')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'full_name', 'total_price', 'created_at')
    search_fields = ('order_id', 'full_name', 'address')
    readonly_fields = ('order_id', 'user', 'full_name', 'address', 'total_price')
    inlines = [OrderItemInline]

@admin.register(HomeSection)
class HomeSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    search_fields = ['title']
    list_filter = ['is_active']
    filter_horizontal = ('products',)

@admin.register(HappyClient)
class HappyClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']
    search_fields = ['name']