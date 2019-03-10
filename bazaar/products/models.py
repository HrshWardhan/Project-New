from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Products(models.Model):
    name=models.CharField(max_length=300)
    description =models.TextField()
    price=models.IntegerField()
    avail=models.IntegerField(default='1')
    quant=models.IntegerField(default='1')
    image = models.ImageField(upload_to='product_image', blank=True)
    date= models.DateTimeField(default=datetime.now())
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
