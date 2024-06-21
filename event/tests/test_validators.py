from django.core.exceptions import ValidationError
from django.test import TestCase

from event.validators import validate_status


class TestValidateStatus(TestCase):
    """ Test the `validate_status` validators """

    def test_success(self):
        """
        Test setting the `validate_status` validator with valid payload.
        """
        try:
            validate_status(1)
        except ValidationError:
            self.fail('Boom! You failed the tests!')

    def test_failed(self):
        """
        Test setting the `validate_status` validator with invalid payload.
        """
        invalid_value = 0

        with self.assertRaises(ValidationError) as error:
            validate_status(invalid_value)

        actual = error.exception.message
        expected = f"{invalid_value} is not a valid choice. It must be either 1 for 'booking' or 2 for 'cancelation'."
        self.assertEqual(actual, expected)
