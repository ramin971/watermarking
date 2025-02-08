from rest_framework import serializers
from .models import Product







class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','image','watermarked_image']
        read_only_fields = ['id','watermarked_image']
        extra_kwargs={'image':{'write_only':True}}