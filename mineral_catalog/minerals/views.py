from django.shortcuts import get_object_or_404, render

from .models import Mineral


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, 'minerals/mineral_list.html', {'minerals': minerals})


def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    image_filename = "minerals/images/{}.jpg".format(mineral.name)
    return render(request,
                  'minerals/mineral_detail.html',
                  {'mineral': mineral,
                   'image_filename': image_filename})