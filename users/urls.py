from users import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'user', viewset=views.UserViewSet, basename="user")
urlpatterns = router.urls
