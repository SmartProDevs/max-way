from django.shortcuts import render
from .models import *
from config.settings import MEDIA_ROOT
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
