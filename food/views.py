from django.shortcuts import render
from .models import *
def index(request):
    categories = Category.objects.all()
    ctx={
        'categories':categories,
    }
    return render(request, 'food/index.html',ctx)

def main_order(request):
    return  render(request, 'product/order.html')
