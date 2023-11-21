from cart import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'cart', viewset=views.CartReadOnlyViewSet,
                basename="cart-read-only")
router.register(r'cart', viewset=views.CartViewSet, basename="cart")
urlpatterns = router.urls
