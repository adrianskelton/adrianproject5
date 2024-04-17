from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')

    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)

    # Function that will be called when a 404 error occurs
def custom_404(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, '404.html', status=404)

# Function that will be called when a 404 error occurs
def custom_400(request):
    """
    Custom 400 error view.
    """
    return render(request, '400.html', status=404)

# Function that will be called when a 500 error occurs
def custom_500(request):
    """
    Custom 500 error view.
    """
    return render(request, '500.html', status=500)