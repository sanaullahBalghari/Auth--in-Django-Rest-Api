from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from django.urls import path
from .views import example_view
from .views import register_user
from store.views import create_product,get_user_product
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',register_user),
    path('api/register/',register_user),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('test_token/', example_view, name='test_token'),
    path('api/add-product/', create_product, name='create_product'),
    path('api/user-products', get_user_product, name='get_user_product'),
]



