from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_classname(self):
        return "CustomUser"
    
    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='user_id') 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_classname(self):
        return "Item"

    def __str__(self):
        return self.name
