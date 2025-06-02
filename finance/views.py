from rest_framework import viewsets
from finance.models.supplier import SupplierCategory
from .serializers import SupplierSerializer, SupplierCategorySerializer
from finance.repository.django_supplier_repository import DjangoSupplierRepository
from rest_framework.response import Response

class SupplierViewSet(viewsets.ViewSet):
    repository = DjangoSupplierRepository()

    def list(self, request):
        suppliers = self.repository.get_all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)


class SupplierCategoryViewSet(viewsets.ModelViewSet):
    queryset = SupplierCategory.objects.all()
    serializer_class = SupplierCategorySerializer