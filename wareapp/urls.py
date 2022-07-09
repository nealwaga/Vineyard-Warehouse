from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views 


urlpatterns = [

    # path ('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token-obtain-pair'),
    # path ('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),

    path('register-user/',views.RegisterView.as_view(),name='register-user'),
    
    path ('registration', jwt_views.TokenObtainPairView.as_view(), name='registration'),
    path ('login', jwt_views.TokenObtainPairView.as_view(), name='login'),

    path ('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    path ('customer', views.CustomerList.as_view(), name='customer'),
    path ('product', views.ProductList.as_view(), name='product'),
    path ('orders', views.OrdersList.as_view(), name='orders'),
    path ('inventory', views.InventoryList.as_view(), name='inventory'),
    path ('price', views.PriceList.as_view(), name='price'),
    path ('order-item', views.OrderItemList.as_view(), name='order-item'),

    path ('add-product', views.AddProductList.as_view(), name='add-product'),
    path ('delete-product', views.DeleteProductList.as_view(), name='delete-product'),
    path ('update-product', views.UpdateProductList.as_view(), name='update-product'),

    path ('update-profile', views.UpdateProfileList.as_view(), name='update-profile'),

    path ('add-inventory', views.AddInventoryList.as_view(), name='add-inventory'),


    path ('add-to-cart', views.AddToCartList.as_view(), name='add-to-cart'),

]