from django.contrib import admin
from .models import Artist

# Register your models here.

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'total_sales', 'website')
    search_fields = ('full_name', 'bio', 'website')