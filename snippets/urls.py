from django.urls import path
from snippets import views

from finance.views import supplier_list, supplier_list_by_tax_id

urlpatterns = [
    path('snippets/', views.snippet_list),
    #path('snippets/<int:pk>/', views.snippet_detail),
    path('suppliers/<str:request_tax_id>/', supplier_list_by_tax_id),
    path('suppliers/', supplier_list)
]