from rest_framework import serializers
from .models import Brand,Category,Item

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id','brand')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','category')

class ItemSerializer(serializers.ModelSerializer):
    #brand_name = serializers.StringRelatedField(many=True)
    #category_name = serializers.StringRelatedField(many=True)
    class Meta:
        model = Item
        fields = ('id','title','image','price','discount','slug','brand_name',
                  'category_name','colour','size','weight','discription','modify_date','expiry_date','create_date')

