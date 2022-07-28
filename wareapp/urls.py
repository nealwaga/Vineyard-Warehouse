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
    
    # path ('registration', jwt_views.TokenObtainPairView.as_view(), name='registration'),
    path ('login', jwt_views.TokenObtainPairView.as_view(), name='login'),

    # path ('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    path ('product', views.ProductList.as_view(), name='product'),
    path ('add-product', views.add_product.as_view(), name='add-product'),
    path ('update-product', views.update_product.as_view(), name='update-product'),
    # path ('delete-product', views.DeleteProductList.as_view(), name='delete-product'),

    path ('orders', views.OrdersList.as_view(), name='orders'),
    path ('order-item', views.OrderItemList.as_view(), name='order-item'),

    path ('inventory', views.InventoryList.as_view(), name='inventory'),
    path ('add-inventory', views.add_inventory.as_view(), name='add-inventory'),

    path ('price', views.PriceList.as_view(), name='price'),
    
    path ('all-users/',views.all_users.as_view(),name='allusers'),
    path ('edit-profile', views.edit_profile.as_view(), name='edit-profile'),
    # path ('customer', views.CustomerList.as_view(), name='customer'),

    path ('add-to-cart', views.CartView.as_view(), name='add-to-cart'),
    path ('empty-carts',views.EmptyCart.as_view(),name='emptycart'),

]