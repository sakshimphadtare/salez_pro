from django.contrib import admin
from .models import Product, Category, Order

# Register Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'stock_quantity')  # Show these fields in the list view
    search_fields = ('name',)  # Add search functionality by name
    list_filter = ('category',)  # Add filter functionality for category

# Register Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show category name in the list view
    search_fields = ('name',)  # Add search functionality by category name

# Register Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'created_at')  # Display product, quantity, total price, and creation date
    search_fields = ('product__name',)  # Search orders by product name
    list_filter = ('created_at',)  # Filter orders by creation date

# Register models with custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)

from .forms import OrderForm

class OrderAdmin(admin.ModelAdmin):
    form = OrderForm  # Use custom form
    list_display = ('product', 'quantity', 'total_price', 'created_at')
    search_fields = ('product__name',)
    list_filter = ('created_at',)
