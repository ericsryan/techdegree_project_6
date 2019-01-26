from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    """Display menu and random mineral."""
    mineral = Mineral.objects.order_by('?').first()
    image_filename = "minerals/images/{}.jpg".format(mineral.name)
    return render(request,
                  'index.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})
