from users import views
from rest_framework import routers
from django.urls import path
urlpatterns = [
    path('favorite/', views.FavoriteProductAPIView.as_view())]
router = routers.SimpleRouter()
router.register(r'user', viewset=views.UserViewSet, basename="user")
router.register(r'user_informathion',
                viewset=views.UserInformathionViewSet, basename="user-informathion")
urlpatterns += router.urls
