from django.db import models
from artists.models import Artist


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    size = models.CharField(
        max_length=2,
        choices=[
            ("xs", "XS"),
            ("s", "S"),
            ("m", "M"),
            ("l", "L"),
            ("xl", "XL"),
        ],
        null=True,
        blank=True,
    )
    price_xs = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    price_s = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                  blank=True)
    price_m = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                  blank=True)
    price_l = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                  blank=True)
    price_xl = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True,
                                 blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True,
                               on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
