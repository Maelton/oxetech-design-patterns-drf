from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from .models import Supplier
from .serializers import SupplierSerializer

@csrf_exempt
def supplier_list_by_tax_id(request, request_tax_id):
    if request.method == 'GET':
        suppliers = Supplier.objects.get(tax_id=request_tax_id)
        serializer = SupplierSerializer(suppliers)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def supplier_list(request):
    if request.method == 'GET':
        suppliers = Supplier.objects.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SupplierSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)