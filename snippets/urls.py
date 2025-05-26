from django.urls import path, include
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list)
]