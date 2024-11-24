from rest_framework import serializers
from .models import User, Password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'master_password_hash']

class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Password
        fields = ['label', 'encrypted_password']
