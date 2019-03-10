from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Products
from .import views
from .views import ArticleDetailView

urlpatterns = [
    url(r'^Products/new$', views.Product, name="ho"),
    url(r'^$',ListView.as_view(queryset=Products.objects.all().order_by("-date")[:8],template_name="Core/home.html")),
    url(r'^Products/(?P<pk>\d+)$', ArticleDetailView.as_view(template_name='products/pro.html')),
]
