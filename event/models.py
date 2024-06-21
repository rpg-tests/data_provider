from django.core.validators import MinValueValidator
from django.db import models

from event.validators import validate_status


class Event(models.Model):
    id = models.BigIntegerField(
        primary_key=True,
        validators=[MinValueValidator(1)]
    )
    hotel_id = models.BigIntegerField(validators=[MinValueValidator(1)])
    room_reservation_id = models.UUIDField()
    timestamp = models.DateTimeField()
    night_of_stay = models.DateField()
    status = models.IntegerField(validators=[validate_status])
