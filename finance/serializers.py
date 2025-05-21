from .models import Supplier
from rest_framework import serializers

import requests

class SupplierSerializer(serializers.ModelSerializer):
    
    api_name = serializers.SerializerMethodField(read_only=True)
    api_address = serializers.SerializerMethodField(read_only=True)
    
    def get_api_name(self, obj):
        api_name_data = requests.get(f'https://receitaws.com.br/v1/cnpj/{obj.tax_id}')
        
        if api_name_data.status_code == 200:
            return api_name_data.json().get('nome')
        
    def get_api_address(self, obj):
        api_address_data = requests.get(f'https://receitaws.com.br/v1/cnpj/{obj.tax_id}')

        if api_address_data.status_code == 200:
            return api_address_data.json().get('logradouro')
        
    class Meta:
        model = Supplier
        fields = ['id', 'name', 'tax_id', 'api_name', 'api_address', 'phone', 'is_active', 'created_at', 'updated_at']
        extra_kwargs = {
            'name': {'write_only': True},
            'tax_id': {'write_only': True},
        }