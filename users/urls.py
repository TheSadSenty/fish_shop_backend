from users import views
from rest_framework import routers
router = routers.SimpleRouter()
router.register(r'user', viewset=views.UserViewSet, basename="user")
router.register(r'user_informathion', viewset=views.UserInformathionViewSet, basename="user-informathion")
urlpatterns = router.urls
