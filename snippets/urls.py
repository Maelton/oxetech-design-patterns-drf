from django.urls import path
from snippets.views.fornecedor import (
    FornecedorViewSet,
)
from snippets.views.lancamento import (
    LancamentoViewSet
)

urlpatterns = [
    path('fornecedores', view=FornecedorViewSet.as_view()),
    path('fornecedores/<int:pk>', view=FornecedorViewSet.as_view()),
    path('lancamentos', view=LancamentoViewSet.as_view()),
    path('lancamentos/<int:pk>', view=LancamentoViewSet.as_view()),
]