from django.shortcuts import render
from django.http import HttpResponse


def mineral_list(request):
    return HttpResponse('Mineral List')


def mineral_detail(request, id):
    return HttpResponse(f'Mineral Detail {id}')
