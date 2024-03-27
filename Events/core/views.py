from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils import timezone

from django.db.models import Q

# from datetime import datetime

from . import models


def event_filter(filter_data):
    search_text = filter_data.get('search-text')
    locations = filter_data.getlist('location')
    topics = filter_data.getlist('topic')

    events = models.Event.objects.all()

    if search_text:
        events = events.filter(Q(title__icontains=search_text) | Q(description__icontains=search_text))

    if locations:
        events = events.filter(location__in=locations)

    if topics:
        events = events.filter(topic__in=topics)

    events_recently = events.filter(event_date__gt=timezone.now())
    events_past = events.filter(event_date__lt=timezone.now())

    return events_recently, events_past


def index(request):
    events_recently, events_past = event_filter(request.GET)

    ctx = {
        'locations': models.Location.objects.all(),
        'topics': models.Topic.objects.all(),
        'events_recently': events_recently,
        'events_past': events_past,
    }
    return render(request, 'core/index.html', ctx)


def event_detail(request, event_pk):
    event = models.Event.objects.get(pk=event_pk)
    return render(request, 'core/event_detail.html', {'event': event})


@login_required
def sub(request):
    if request.method == 'POST':
        event_pk = request.POST.get('event')
        event = models.Event.objects.get(pk=event_pk)
        event.users.add(request.user)
        event.save()
        return redirect(reverse('event_detail', kwargs={'event_pk': event_pk}))
    else:
        return redirect(reverse('home'))
