from rest_framework import generics

from event.filters import EventFilter
from event.models import Event
from event.serializers import EventSerializer


class EventListView(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all().order_by('timestamp')
