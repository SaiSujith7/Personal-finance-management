from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Expense(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.CharField(max_length=266)
    date=models.CharField(max_length=100)
    amount=models.CharField(max_length=100)

    def __str__(self):
        return self.category

    class Meta:
        ordering:['-date']
    
class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name
