from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',null=True)
    watermarked_image = models.ImageField(upload_to='images/watermarked/',null=True,blank=True)


