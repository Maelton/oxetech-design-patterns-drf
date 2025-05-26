from .models import Supplier, SupplierCategory
from rest_framework import serializers

class SupplierSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Supplier
        fields = '__all__'

class SupplierCategorySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = SupplierCategory
        fields = '__all__'