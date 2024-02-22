from django.shortcuts import render

from . import models


def index(request):
    events = models.Event.objects.all()
    return render(request, 'base.html', {'events': events})


def event_detail(request, event_pk):
    event = models.Event.objects.get(pk=event_pk)
    return render(request, 'event_detail.html', {'event': event})

