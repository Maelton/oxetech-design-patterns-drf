from django.db import models
from django.core.validators import MinLengthValidator

class Supplier(models.Model):
    name = models.CharField()
    tax_id = models.CharField(max_length=14, validators=[MinLengthValidator(11)])
    email = models.EmailField()
    phone = models.CharField()
    address = models.CharField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)