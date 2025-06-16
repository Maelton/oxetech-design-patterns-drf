from django.urls import path
from snippets.views.fornecedor import FornecedorViewSet

urlpatterns = [
    path('fornecedores', view=FornecedorViewSet.as_view()),
    path('fornecedores/<int:pk>', view=FornecedorViewSet.as_view()),
]