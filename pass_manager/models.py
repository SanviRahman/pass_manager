from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from cryptography.fernet import Fernet

class User(AbstractUser):
    master_password_hash = models.CharField(max_length=255)


class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    encrypted_password = models.TextField()

    def encrypt_password(self, password, key):
        cipher = Fernet(key)
        self.encrypted_password = cipher.encrypt(password.encode()).decode()

    def decrypt_password(self, key):
        cipher = Fernet(key)
        return cipher.decrypt(self.encrypted_password.encode()).decode()

