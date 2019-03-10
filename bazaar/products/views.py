from django.shortcuts import render,redirect
from .forms import ProductsForm
from .models import Products
from django.views.generic.detail import DetailView
from django.utils import timezone

class ProductCreate(ProductsForm):
    model = Products
    form_class = ProductsForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(ProductCreate, self).form_valid(form)

def  Product(request):
    if not request.user.is_authenticated():
        return redirect('/login/')
    else:
        if request.method == 'POST':
            f = ProductsForm(request.POST)
            if f.is_valid():
                f.save()
                return redirect('register')

        else:
            f = ProductsForm()

        return render(request, 'Products/reg_form.html', {'form': f})


class ArticleDetailView(DetailView):

    model = Products

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
