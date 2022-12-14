from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from course.models import Course
from account.models import Account
from .models import Cart, CartItem
# Create your views here.


def create_cart(request):
    if request.user.is_authenticated:
        cart_exist = Cart.objects.filter(
            user__username=request.user.username).exists
        if cart_exist:
            cart = Cart(user=request.user)
            cart.save()


def add_cart(request, course_slug=None):
    current_user = request.user
    course = Course.objects.get(slug=course_slug)
    is_exists_cart_item = CartItem.objects.filter(
        course=course, cart__user=current_user).exists

    if current_user.is_authenticated:
        cart = Cart.objects.get(user=current_user)
        if not is_exists_cart_item:
            cart_item = CartItem.objects.create(course=course, cart=cart)
            cart_item.save()
    return redirect('cart')


def remove_cart(request):
    pass


def remove_cart_item(request):
    pass


def cart(request):
    return render(request, 'cart/cart.html')
