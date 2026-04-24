# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name')

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')
        extra_kwargs = {
            'full_name': {'required': True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['email'], # Username হিসেবে ইমেইলই রাখছি
            full_name=validated_data.get('full_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user