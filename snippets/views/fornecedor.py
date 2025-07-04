from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from snippets.tasks import add
from snippets.models.fornecedor import Fornecedor
from snippets.serializers.fornecedor import FornecedorSerializer

class FornecedorViewSet(APIView):
    def get_object(self, pk):
        try:
            return Fornecedor.objects.get(pk=pk)
        except Fornecedor.DoesNotExist:
            raise Http404
    
    def get(self, request, pk=None):
        add.delay(10, 10)
        
        if pk:
            fornecedor = Fornecedor.objects.get(id=pk)
            
            serializer = FornecedorSerializer(fornecedor)
            return JsonResponse(serializer.data, safe=False)

        fornecedores = Fornecedor.objects.all()
        serializer = FornecedorSerializer(fornecedores, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        serializer = FornecedorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = FornecedorSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        print(pk)
        fornecedor = self.get_object(pk)
        fornecedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
