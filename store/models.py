from django.db import models
from django.conf import settings

# store/models.py এ যোগ করুন
class HomeSection(models.Model):
    title = models.CharField(max_length=100) # সেকশনের নাম (যেমন: Gaming Gear)
    order = models.PositiveIntegerField(default=0) # সেকশনটি কত নম্বরে দেখাবে
    is_active = models.BooleanField(default=True)
    products = models.ManyToManyField('Product', related_name='home_sections')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    # নতুন ফিল্ড: ক্যাটাগরির আইকনের জন্য
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True) 

    def __str__(self):
        return self.name
    
class Banner(models.Model):
    PLACEMENT_CHOICES = (
        ('hero', 'Hero Slider (Top)'),
        ('campaign', 'Full Width Campaign Banner'),
        ('mid_promo_left', 'Mid Promo (Left Side)'),
        ('mid_promo_right', 'Mid Promo (Right Side)'),
        ('featured_large', 'Featured Grid (Large Vertical Card)'),
        ('featured_small_top', 'Featured Grid (Small Top Card)'),
        ('featured_small_bottom', 'Featured Grid (Small Bottom Card)'),
    )
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    placement = models.CharField(max_length=30, choices=PLACEMENT_CHOICES, default='hero')
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_placement_display()})"

class Brand(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    logo = models.ImageField(upload_to='brands/', blank=True, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    
    # UI Sections Flags
    is_exclusive = models.BooleanField(default=False)
    is_top_deal = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    is_feature = models.BooleanField(default=False)
class Banner(models.Model):
    PLACEMENT_CHOICES = (
        ('hero', 'Hero Slider'),
        ('campaign', 'Full Width Campaign Banner'),
        ('mid_promo_left', 'Mid Promo (Left Side)'),
        ('mid_promo_right', 'Mid Promo (Right Side)'),
        ('featured_large', 'Featured Grid (Large Card)'),
        ('featured_small_top', 'Featured Grid (Small Top Card)'),
        ('featured_small_bottom', 'Featured Grid (Small Bottom Card)'),
    )
    
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    placement = models.CharField(max_length=30, choices=PLACEMENT_CHOICES, default='hero') # এই ফিল্ডটি আসল ম্যাজিক!
    button_text = models.CharField(max_length=50, blank=True, null=True)
    button_link = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

# WhatsApp Checkout-এর জন্য অর্ডার সেভ রাখার মডেল
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    order_id = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=255)
    address = models.TextField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.order_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)