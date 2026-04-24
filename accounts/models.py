from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    
    # ইমেইল হবে প্রাইমারি লগইন ফিল্ড
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # 'username' জ্যাঙ্গোর জন্য রিকোয়ার্ড, তবে আমরা ইমেইল দিয়ে লগইন করাবো

    def __str__(self):
        return self.email