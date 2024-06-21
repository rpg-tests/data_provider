import uuid

from model_bakery import baker
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.test import APIRequestFactory, APITestCase

from event.models import Event
from event.serializers import EventSerializer


class TestEventSerializer(APITestCase):
    """ Test the `EventSerializer` """

    def setUp(self):
        self.factory = APIRequestFactory()

    def test_serialization(self):
        """
        Test output of the `Event` serialization.
        """
        instance = baker.make(Event)

        actual = EventSerializer(instance=instance).data
        expected = {
            'id': instance.id,
            'hotel_id': instance.hotel_id,
            'room_id': str(instance.room_reservation_id),
            'timestamp': instance.timestamp.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'night_of_stay': instance.night_of_stay.strftime('%Y-%m-%d'),
            'rpg_status': instance.status,
        }
        self.assertDictEqual(expected, actual)

    def test_deserialization_success(self):
        """
        Test the `Event` deserialization with valid payload.
        """
        payload = {
            'id': 1,
            'hotel_id': 1,
            'room_id': str(uuid.uuid4()),
            'timestamp': '2024-06-11T14:15:22Z',
            'night_of_stay': '2024-06-12',
            'rpg_status': 1
        }

        request = self.factory.post('/')
        deserializer = EventSerializer(
            data=payload,
            context={'request': request}
        )

        try:
            deserializer.is_valid(raise_exception=True)
        except ValidationError:
            self.fail('Gotcha! You fail the test!')

    def test_deserialization_failed(self):
        """
        Test the `Event` deserialization with invalid payload.
        """
        payload = {
            'id': 1,
            'hotel_id': 1,
            'room_id': str(uuid.uuid4()),
            'timestamp': '2024-06-11T14:15:22Z',
            'night_of_stay': '2024-06-12',
            'rpg_status': 0
        }

        request = self.factory.post('/')
        deserializer = EventSerializer(
            data=payload,
            context={'request': request}
        )

        with self.assertRaises(ValidationError) as error:
            deserializer.is_valid(raise_exception=True)

        self.assertEqual(
            error.exception.detail,
            {
                'rpg_status': [
                    ErrorDetail(
                        string="0 is not a valid choice. It must be either 1 for 'booking' or 2 for 'cancelation'.",
                        code='invalid'
                    )
                ]
            }
        )
