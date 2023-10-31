from django.urls import path
from products import views

urlpatterns = [
    path('products/<int:id>/', views.ProductsDetail.as_view()),
    path('category/<int:id>/', views.CategoryDetail.as_view()),
    path('category/', views.CategoryList.as_view()),
    path('products/', views.ProductsList.as_view())
]
