from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30,null=False)
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
        null=False,
        blank=False
    )
    class Meta:
        ordering=['-price','-name']
    
    def __str__(self):
        return self.name