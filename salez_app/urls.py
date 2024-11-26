from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for the API views
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)  # Register the product viewset
router.register(r'orders', views.OrderViewSet)  # Register the order viewset
router.register(r'category', views.CategoryViewSet)  # Register the category viewset


# Add the URL patterns for non-API views (e.g., templates)
urlpatterns = [
    path('product_list/', views.product_list, name='product_list'),
    path('order_list/', views.order_list, name='order_list'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/<int:pk>/delete/', views.order_delete, name='order_delete'),
    path('product/create/', views.product_create, name='product_create'),
    path('product/<int:pk>/update/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]

# Include the router URLs for the API endpoints
urlpatterns += router.urls  # This will add the '/api/products/' and '/api/orders/' routes
