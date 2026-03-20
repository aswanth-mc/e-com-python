from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required


# Product Listing
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


#View Cart
@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = CartItem.objects.filter(cart=cart)

    total = sum(item.total_price() for item in items)

    return render(request, 'cart.html', {
        'items': items,
        'total': total
    })


#Add to Cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        return redirect('product_list')

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': quantity}   # ✅ FIX HERE
    )

    if not created:
        item.quantity += quantity
        item.save()

    return redirect('view_cart')


#Update Cart
@login_required
def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)

    quantity = int(request.POST.get('quantity', 1))

    if quantity <= 0:
        item.delete()
    else:
        item.quantity = quantity
        item.save()

    return redirect('view_cart')


#Remove Item
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('view_cart')