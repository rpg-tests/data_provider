from django.core.exceptions import ValidationError


def validate_status(value):
    STATUS_BOOKING = 1
    STATUS_CANCELATION = 2

    if value not in [STATUS_BOOKING, STATUS_CANCELATION]:
        raise ValidationError(
            f"{value} is not a valid choice. "
            f"It must be either {STATUS_BOOKING} for 'booking' "
            f"or {STATUS_CANCELATION} for 'cancelation'."
        )
