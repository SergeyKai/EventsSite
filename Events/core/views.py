import json
from functools import wraps

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.utils import timezone

from django.db.models import Q

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


"""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            if test_func(request.user):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
            # If the login url is the same scheme and net location then just
            # use the path as the "next" url.
            login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if (not login_scheme or login_scheme == current_scheme) and (
                not login_netloc or login_netloc == current_netloc
            ):
                path = request.get_full_path()
            from django.contrib.auth.views import redirect_to_login

            return redirect_to_login(path, resolved_login_url, redirect_field_name)

        return _wrapper_view
"""


def sub_decorator(view_func):
    @wraps(view_func)
    def _wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)

        if request.method == 'POST':
            data = json.loads(request.body)
            event_pk = data.get('event')
            path = reverse('event_detail', kwargs={'event_pk': event_pk})
            resolved_login_url = resolve_url(settings.LOGIN_URL)

            from django.contrib.auth.views import redirect_to_login
            return redirect_to_login(path, resolved_login_url, 'next')
        else:
            return HttpResponse(status=405)

    return _wrapper


@sub_decorator
def sub(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_pk = data.get('event')
        event = models.Event.objects.get(pk=event_pk)
        event.users.add(request.user)
        event.save()
        return JsonResponse({'status': 'success'})
    else:
        return HttpResponse(status=405)


@login_required
def un_sub(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        event_pk = data.get('event')
        try:
            event = request.user.events.get(pk=event_pk)
            request.user.events.remove(event)
        except models.Event.DoesNotExist:
            pass
        return JsonResponse({'status': 'success'})
    else:
        return HttpResponse(status=405)
