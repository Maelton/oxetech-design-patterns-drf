from django.db import models
from django.core.validators import MinLengthValidator

class Supplier(models.Model):
    name = models.CharField("Name / Business Name", max_length=255)
    tax_id = models.CharField("Tax ID (CNPJ/CPF)", max_length=20, unique=True, validators=[MinLengthValidator(11)])
    email = models.EmailField("Email", unique=True)
    phone = models.CharField("Phone", max_length=20, blank=True)
    address = models.TextField("Address")
    contact_person = models.CharField("Contact Person", max_length=255, blank=True)
    category = models.ForeignKey('SupplierCategory', on_delete=models.PROTECT)
    is_active = models.BooleanField("Active", default=True)
    created_at = models.DateTimeField("Created At", auto_now_add=True)
    updated_at = models.DateTimeField("Updated At", auto_now=True)

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"
        ordering = ["name"]

    def __str__(self):
        return self.name

class SupplierCategory(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    description = models.TextField("Description", blank=True)

    class Meta:
        verbose_name = "Supplier Category"
        verbose_name_plural = "Supplier Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name
