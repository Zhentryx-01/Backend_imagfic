from django.db import models
from django.contrib.auth.models import AbstractUser


class ImageCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    category = models.ForeignKey(ImageCategory, related_name='images', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image_file = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
