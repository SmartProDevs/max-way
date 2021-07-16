from django import forms
from food.models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),

        }

class ProductForm(forms.ModelForm):
    model = Product
    fields = "__all__"