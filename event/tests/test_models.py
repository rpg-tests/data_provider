from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker

from event.models import Event


class TestEvent(TestCase):
    """ Test the `Event` models """

    def setUp(self):
        self.all_fields = [f.name for f in Event._meta.fields]

    def test_clean_fields_status_success(self):
        """
        Test setting the `status` field with valid payload.
        """
        instance = baker.prepare(Event, status=1)

        checked_fields = ['status']
        excluded_fields = set(self.all_fields) - set(checked_fields)

        try:
            instance.clean_fields(exclude=excluded_fields)
        except ValidationError:
            self.fail('Boom! You failed the tests!')

    def test_clean_fields_status_failed(self):
        """
        Test setting the `status` field with invalid payload.
        """
        invalid_value = 0
        instance = baker.prepare(Event, status=invalid_value)

        checked_fields = ['status']
        excluded_fields = set(self.all_fields) - set(checked_fields)

        with self.assertRaises(ValidationError) as error:
            instance.clean_fields(exclude=excluded_fields)

        actual = error.exception.message_dict
        expected = {
            'status': [
                f"{invalid_value} is not a valid choice. "
                "It must be either 1 for 'booking' or 2 for 'cancelation'."
            ]
        }
        self.assertDictEqual(actual, expected)
