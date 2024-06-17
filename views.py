from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import JsonResponse
import json

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {'product': product})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        # In a real application, you would handle adding the product to the user's cart
        return JsonResponse({'message': 'Product added to cart!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)
