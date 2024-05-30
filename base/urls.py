from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path("",views.getAllProducts, name="allproduct"),
    path("all-products", lambda request: redirect('allproduct'), name="redirect_to_allproduct"),
    path("get-product/<str:pk>/",views.getProductbyId,name="getproduct"),
    path("create-product/",views.create_product,name="create-product"),
    path('update-product/<str:pk>/',views.update_product,name="update-product"),
    path('delete-product/<str:pk>/',views.deleteproduct,name="delete-product"),    
]