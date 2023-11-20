from cart import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'cart', viewset=views.CartViewSet, basename="cart")
urlpatterns = router.urls
