from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from .services import *
from config.settings import MEDIA_ROOT

def home_page(request):
    if request.GET:
        product = get_product_by_id(request.GET.get("product_id", 0))
        return JsonResponse(product)

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    ctx={
        'categories':categories,
        'products': products,
        'MEDIA_ROOT':MEDIA_ROOT
    }
    return render(request, 'food/index.html',ctx)

def main_order(request):
    return  render(request, 'food/order.html')
