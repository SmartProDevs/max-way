from django.shortcuts import render
from food.models import *
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from . import forms

def login_required_decarator(func):
    return login_required(func, login_url='login_page')

login_required_decarator
def main_dashboard(request):
    categories = Category.objects.all()
    products = Category.objects.all()
    ctx = {
        "counts":{
            "categories":len(categories),
            "products": len(products)
        },

    }
    return render(request, 'dashboard/index.html',ctx)

def login_page(request):
    if request.POST:
        username =request.POST.get("username",None)
        password = request.POST.get("password", None)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request,'main_dashboard')
    return redirect(request,'login_page')

@login_required_decarator
def logout_page(request):
    logout(request)
    return redirect('login_page')

@login_required_decarator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories':categories
    }
    return render(request, "dashboard/category/list.html",ctx)

@login_required_decarator
def category_create(request):
    model = Category()
    form = forms.CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html',ctx)

@login_required_decarator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = forms.CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html',ctx)

@login_required_decarator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return  redirect("category_list")
#############product#########################################
@login_required_decarator
def category_list(request):
    categories = Category.objects.all()
    ctx = {
        'categories':categories
    }
    return render(request, "dashboard/category/list.html",ctx)

@login_required_decarator
def category_create(request):
    model = Category()
    form = forms.CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html',ctx)

@login_required_decarator
def category_edit(request,pk):
    model = Category.objects.get(pk=pk)
    form = forms.CategoryForm(request.POST or None, instance=model)

    if request.POST and form.is_valid():
        form.save()
        return redirect('category_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request, 'dashboard/category/form.html',ctx)

@login_required_decarator
def category_delete(request,pk):
    model = Category.objects.get(pk=pk)
    model.delete()
    return  redirect("category_list")

@login_required_decarator
def product_list(request):
    model = Product.objects.all()
    ctx = {
        'model':model
    }
    return render(request, 'dashboard/product/form.html',ctx)

@login_required_decarator
def product_create(request):
    model = Product()
    form = forms.ProductForm(request.POST or None, instance = model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request,'dashboard/product/form.html',ctx)

@login_required_decarator
def product_edit(request,pk):
    model = Product.objects.get(pk=pk)
    form = forms.ProductForm(request.POST or None, instance = model)
    if request.POST and form.is_valid():
        form.save()
        return redirect('product_list')
    ctx = {
        'model':model,
        'form': form
    }
    return render(request,'dashboard/product/form.html',ctx)

def product_delete(request,pk):
    model = Product.objects.get(pk=pk)
    model.delete()
    return redirect('product_list')