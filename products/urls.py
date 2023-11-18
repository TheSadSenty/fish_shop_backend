from products import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'products', viewset=views.ProductViewSet, basename="product")
router.register(r'categories', viewset=views.CategoryViewSet,
                basename="category")
urlpatterns = router.urls
