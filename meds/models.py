from django.db import models
from django.contrib.auth.models import User

class Medicine(models.Model):
    CATEGORY=(
        ('Internal','Internal'),
        ('External','External')
    )
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    description=models.CharField(max_length=200)
    category=models.CharField(max_length=100, choices=CATEGORY)
    
