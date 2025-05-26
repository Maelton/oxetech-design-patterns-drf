# finance/urls.py
from rest_framework.routers import DefaultRouter
from .views import SupplierViewSet, SupplierCategoryViewSet

router = DefaultRouter()
router.register('suppliers', SupplierViewSet)
router.register('supplierCategories', SupplierCategoryViewSet)

urlpatterns = router.urls
