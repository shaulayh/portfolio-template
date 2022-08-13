from django.contrib import admin

# Register your models here.
from django.utils.html import format_html

from .models import PortfolioImages


class PortfolioImagesAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image_file.url))

    image_tag.short_description = 'Image'

    list_display = ['image_tag', 'image_caption', 'upload_date']
    readonly_fields = ['image_tag']


admin.site.register(PortfolioImages, PortfolioImagesAdmin)
