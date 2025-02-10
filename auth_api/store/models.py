from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10, decimal_places=2)
    discription=models.TextField(null=True, blank=True)
    seller=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name