from django import forms
from .models import Product

class ProductModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class UpdateProductForm(forms.ModelForm):
    product_select = ProductModelChoiceField(queryset=Product.objects.all().order_by('name'),
                                             required=False, label="Выберите продукт", empty_label="Выберите продукт")

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity']
        labels = {
            'name': 'Название товара',
            'description': 'Описание',
            'price': 'Цена',
            'quantity': 'Количество',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Введите описание товара'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите цену товара'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество товара'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'image']
