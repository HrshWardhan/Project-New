from django.forms import ModelForm
from .models import Products

class ProductsForm(ModelForm):
    class Meta:
        model = Products
        fields =['name','description','price','quant','image','User']

    def save(self, commit=True):
        Products = super(ProductsForm, self).save(commit=True)

        return Products
