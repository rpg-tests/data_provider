from django.utils.timezone import now
from model_bakery import baker
from rest_framework.test import APIRequestFactory, APITestCase

from event.filters import EventFilter
from event.models import Event
from event.serializers import EventSerializer
from event.views import EventListView


class TestEventListView(APITestCase):
    """ Test the `EventListView` """

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = EventListView()

    def test_get_serializer_class(self):
        self.assertEqual(
            self.view.get_serializer_class(),
            EventSerializer
        )

    def test_filterset_class(self):
        self.assertEqual(
            self.view.filterset_class,
            EventFilter
        )

    def test_get_queryset(self):
        """
        Test the `get_queryset` method returns `Event` instances
        sorted by `timestamp` in ascending order.
        """
        today = now()

        event_1 = baker.make(Event, timestamp=today.replace(hour=12))
        event_2 = baker.make(Event, timestamp=today.replace(hour=9))
        event_3 = baker.make(Event, timestamp=today.replace(hour=16))

        self.view.request = self.factory.get('/')

        actual = self.view.get_queryset()
        expected = [event_2, event_1, event_3]
        self.assertQuerysetEqual(
            actual,
            expected,
            lambda item: item,
            ordered=True
        )
