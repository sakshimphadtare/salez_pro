from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Order , Category
from .forms import ProductForm, OrderForm
from .serializers import ProductSerializer, OrderSerializer , CategorySerializer 

# View for displaying all products (Read)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'salez_app/product_list.html', {'products': products})

# View for creating a product (Create)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'salez_app/product_form.html', {'form': form})

# View for updating a product (Update)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'salez_app/product_form.html', {'form': form})

# View for deleting a product (Delete)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'salez_app/product_confirm_delete.html', {'product': product})

# View for displaying all orders (Read)
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'salez_app/order_list.html', {'orders': orders})

# View for creating an order (Create)
def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = order.product.price * order.quantity
            order.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'salez_app/order_form.html', {'form': form})

# View for deleting an order (Delete)
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'salez_app/order_confirm_delete.html', {'order': order})

# ViewSet for Product API
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# ViewSet for Order API
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# API to get all products or create a new product
@api_view(['GET', 'POST'])
def product_api(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# API to get all orders or create a new order
@api_view(['GET', 'POST'])
def order_api(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            product = Product.objects.get(id=serializer.validated_data['product'].id)
            quantity = serializer.validated_data['quantity']
            serializer.validated_data['total_price'] = product.price * quantity
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
