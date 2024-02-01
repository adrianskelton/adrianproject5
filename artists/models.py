from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    bio = models.TextField()
    total_sales = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='artist_images/')
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.full_name