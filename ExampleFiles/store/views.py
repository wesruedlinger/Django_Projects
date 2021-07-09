from django.shortcuts import render, get_object_or_404
from .models import ProductCategory, Product
from cart.forms import CartAddProductForm


def store(request, category_slug=None):
    products = Product.objects.all()
    category = None
    categories = ProductCategory.objects.all()
    if category_slug:
        category = get_object_or_404(ProductCategory, slug=category_slug)
        products = products.filter(category=category)
    else:
        category = None
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'store/store.html', context)


def product_details(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    context = {'product': product, 'cart_product_form': cart_product_form}
    return render(request, 'store/product_details.html', context)