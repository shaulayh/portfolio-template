from django.http import HttpResponse
from django.shortcuts import render

# images
from .models import PortfolioImages

portfolio_image = PortfolioImages.objects.all()

context = {
    'portfolio_images': portfolio_image
}


# Create your views here.
def index(request):
    return render(request, "index.html", context)


def show(request):
    return render(request, "index2.html", context)
