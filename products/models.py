from django.db import models

# Create your models here.
class Products(models.Model):
    title = (
        models.CharField(max_length=120) # required
    )  # mapped  to database and need to inherit from default class
    description = models.TextField(blank=True,null=True)  # mapped  to database
    price = models.TextField()  # mapped  to database
    active=models.TextField()