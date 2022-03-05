from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Event


def details(request, id):
    event= get_object_or_404(Event, id=id)
    return render(request, 'events/details.html', {'events': event})


def list(request):
    today = datetime.today()

    events = Event.objects.filter(
        datetime__gte=today).order_by("datetime")
    return render(request, 'events/list.html', {"events": events})
