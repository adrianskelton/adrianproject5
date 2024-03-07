from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Update prices for all products'

    def handle(self, *args, **options):
        # Update prices for all products here
        for product in Product.objects.all():
            # Set your logic to update prices as needed
            product.price_xs = 150
            product.price_s = 200
            product.price_m = 250
            product.price_l = 300
            product.price_xl = 350
            product.save()

        self.stdout.write(self.style.SUCCESS('Prices updated successfully.'))