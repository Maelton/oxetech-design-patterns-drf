from django.urls import path
from snippets.views.fornecedor import (
    FornecedorViewSet,
)
from snippets.views.lancamento import (
    LancamentoViewSet
)
from snippets.views.categoria import (
    CategoriaViewSet
)
from snippets.views.forma_pagamento import (
    FormaPagamentoViewSet
)

urlpatterns = [
    path('fornecedores', view=FornecedorViewSet.as_view()),
    path('fornecedores/<int:pk>', view=FornecedorViewSet.as_view()),
    
    path('lancamentos', view=LancamentoViewSet.as_view()),
    path('lancamentos/<int:pk>', view=LancamentoViewSet.as_view()),
    
    path('categorias/', view=CategoriaViewSet.as_view()),
    path('categorias/<int:pk>/', view=CategoriaViewSet.as_view()),
    
    path('formas-pagamento/', view=FormaPagamentoViewSet.as_view()),
    path('formas-pagamento/<int:pk>/', view=FormaPagamentoViewSet.as_view()),
]