from django import forms
from .models import Product, Order

# Form for creating and updating a Product
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'stock_quantity']  # Adjust fields based on your model

# Form for creating and updating an Order
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'quantity', 'total_price']
    
    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get("quantity")
        product = cleaned_data.get("product")
        
        if quantity and product:
            cleaned_data["total_price"] = product.price * quantity
        
        return cleaned_data
