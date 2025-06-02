# finance/urls.py
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, SupplierCategoryViewSet

router = DefaultRouter()
router.register('suppliers', SupplierViewSet, basename='supplier')
router.register('supplierCategories', SupplierCategoryViewSet, basename='supplierCategory')

urlpatterns = router.urls
