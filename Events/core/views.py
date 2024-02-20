from django.shortcuts import render

from . import models


def index(request):
    events = models.Event.objects.all()
    return render(request, 'base.html', {'events': events})
