from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Oh8MjAYK60dzMLR2s3k6AOgXzBGT0wbKPAeXlJuyiRDzETvqthEVHlrZsCkLFxAGwSgIxV6ftEKKFxCkvnk8Xxg00MA33jRTR',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)