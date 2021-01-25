from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
# Create your views here.
from .forms import ProductsForm

def product_create_view(request):
# to save data from html use POST with {% csrf_token %}
    context = {}
    return render(request, "products/product_create_view.html", context)

def product_detail_view(request):
    obj = Products.objects.get(id=3)
    context={
        "object":obj
    }
    return render(request, "products/product_detial.html", context)