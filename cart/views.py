from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, response
from .models import Cart, CartItem
from shop.models import Product
from users.models import User

from main import utils



@login_required
def get_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items_with_total = []
    total_quantity = 0
    for item in cart.cart_items.order_by("-id"):
        total = item.quantity * item.product.price_with_discount
        total_discounted_price = item.quantity * (item.product.price - item.product.price_with_discount)

        cart_items_with_total.append({
            'item': item,
            'product': item.product,
            'quantity': item.quantity,
            'price': item.product.price_with_discount,
            'total': total,
            'total_discounted_price': total_discounted_price,
        })
        total_quantity += item.quantity

    total_price = sum(item['total'] for item in cart_items_with_total)

    context = {
        'cart': cart,
        'cart_items_with_total': cart_items_with_total,
        'total_price': total_price,
        'cart_total_quantity': total_quantity,
        'cart_total_price': total_price,
    }

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'total_quantity': total_quantity,
            'cart_total_price': total_price
        })
    return render(request, "cart.html", context)



@login_required
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = request.POST.get("quantity", 1)

        cart, created = Cart.objects.get_or_create(user=request.user)

        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
        )

        if created:
            cart_item.quantity = int(quantity)
        else:
            cart_item.quantity += int(quantity)
        cart_item.save()

        return JsonResponse({'success': True, 'message': 'Product added to favourites!'})

    return JsonResponse({'success': False, 'message': 'Invalid request method.'})



@login_required
def update_cart_item(request, product_id):

    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, id=product_id)

    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity', 1))
        cart_item.quantity = new_quantity
        cart_item.save()

    item_total = cart_item.quantity * cart_item.product.price_with_discount
    cart_total = sum(item.quantity * item.product.price_with_discount for item in cart.cart_items.all())

    return JsonResponse({
        'item_total': item_total,
        'cart_total': cart_total,
    })


@login_required
def delete_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, product_id=product_id)
    cart_item.delete()
    return redirect(request.META.get("HTTP_REFERER", "/"))


@login_required
def delete_cart_items(request):
    print(request.POST)
    if request.method == "POST":
        item_ids= request.POST.get("item_ids").split(",")
        CartItem.objects.filter(id__in=item_ids).delete()
    return response.HttpResponse(status=200)


def get_cart_items(user):
    try:
        cart = Cart.objects.get(user=user)  # This assumes a OneToOneField or ForeignKey from Cart to User
        return cart.cart_items.all()  # Correctly using the related name 'cart_items' to get CartItems
    except Cart.DoesNotExist:
        return []  # If no cart is found, return an empty list


@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_items_with_total = []
    total_quantity = 0
    total_discount = 0  # Initialize total discount
    subtotal_price = 0  # Initialize subtotal price (price without discount)

    for item in cart.cart_items.order_by("-id"):
        product = item.product
        price = product.price
        price_with_discount = product.price_with_discount
        total = item.quantity * price_with_discount

        # Calculate the discount for each product and sum it up
        item_discount = item.quantity * (price - price_with_discount)
        total_discount += item_discount

        # Calculate the subtotal price (price without discount)
        if product.discount > 0:
            subtotal_price += item.quantity * price
        else:
            subtotal_price += total  # No discount, use total directly

        cart_items_with_total.append({
            'item': item,
            'product': product,
            'quantity': item.quantity,
            'price': price_with_discount,
            'total': total,
            'total_discounted_price': item_discount,
        })

        total_quantity += item.quantity

    total_price = sum(item['total'] for item in cart_items_with_total)

    context = {
        'cart_items_with_total': cart_items_with_total,
        'total_price': total_price,
        'cart_total_quantity': total_quantity,
        'total_discount': total_discount,
        'subtotal_price': subtotal_price,
    }

    emails = User.objects.values_list("email", flat=True)

    for email in emails:
        subject = "Your Personalized Subject Here"

        message = f"""
        Dear {email},
        This is a sample email to demonstrate how to send structured emails in Django.
        Thank you for being a valued member of our community.
        Best regards,
        Your Website Team
        """

        recipient_list = [email]

        # Send the email
        utils.send_message(
            subject=subject,
            message=message,
            recipient_list=recipient_list,
        )

    return render(request, "checkout.html", context)
