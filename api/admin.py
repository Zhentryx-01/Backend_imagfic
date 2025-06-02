from django.contrib import admin
from .models import ImageCategory, Image, CustomUser

# Register your models here.
admin.site.register([ImageCategory, Image, CustomUser])