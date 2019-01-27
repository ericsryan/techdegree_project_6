from django.shortcuts import render

from minerals.models import Mineral


def index(request):
    """Display menu and random mineral."""
    return render(request, 'index.html')
