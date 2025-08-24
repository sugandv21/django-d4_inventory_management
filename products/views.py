from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    return render(request, "products/layout/home.html")

# List
def product_list(request):
    products = Product.objects.all()
    return render(request, "products/layout/product_list.html", {"products": products})

# Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "products/layout/product_detail.html", {"product": product})

# Create
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()
    return render(request, "products/layout/product_form.html", {"form": form})

# Update
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("product_detail", pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, "products/layout/product_form.html", {"form": form})

# Delete
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "products/layout/product_confirm_delete.html", {"product": product})
