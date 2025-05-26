from rest_framework import viewsets
from .models import Supplier, SupplierCategory
from .serializers import SupplierSerializer, SupplierCategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierCategoryViewSet(viewsets.ModelViewSet):
    queryset = SupplierCategory.objects.all()
    serializer_class = SupplierCategorySerializer