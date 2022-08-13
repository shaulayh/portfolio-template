from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class PortfolioImages(models.Model):
    image_file = models.ImageField(upload_to='portfolio_images')
    image_caption = models.CharField(max_length=100)
    upload_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f'image {self.id} + {self.image_caption}'
