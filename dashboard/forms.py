from django import forms
from food.models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = "__all__"

class ProductForm(forms.ModelForm):
    model = Product
    fields = "__all__"