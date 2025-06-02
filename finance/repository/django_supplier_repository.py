from .supplier_repository import SupplierRepositoryInterface
from finance.models.supplier import Supplier

class DjangoSupplierRepository(SupplierRepositoryInterface):
    
    def get_all(self):
        return Supplier.objects.all()
    
    def get_by_id(self, supplier_id):
        return Supplier.objects.filter(id=supplier_id).first()
    
    def create(self, data):
        return Supplier.objects.create(**data)
    
    def update(self, supplier_id, data):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            for key, value in data.items():
                setattr(supplier, key, value)
            supplier.save()
        return supplier

    def delete(self, supplier_id):
        supplier = self.get_by_id(supplier_id)
        if supplier:
            supplier.delete()
        return supplier
