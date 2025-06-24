from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import JsonResponse, Http404

from snippets.models.lancamento import FormaPagamento
from snippets.serializers.forma_pagamento import FormaPagamentoSerializer

class FormaPagamentoViewSet(APIView):
    def get_object(self, pk):
        try:
            return FormaPagamento.objects.get(pk=pk)
        except FormaPagamento.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            forma = self.get_object(pk)
            serializer = FormaPagamentoSerializer(forma)
            return JsonResponse(serializer.data, safe=False)

        formas = FormaPagamento.objects.all()
        serializer = FormaPagamentoSerializer(formas, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        serializer = FormaPagamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        forma = self.get_object(pk)
        serializer = FormaPagamentoSerializer(forma, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        forma = self.get_object(pk)
        forma.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
