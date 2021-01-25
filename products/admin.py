from django.contrib import admin

# Register your models here.

from .models import Products

#to view Products
admin.site.register(Products)
