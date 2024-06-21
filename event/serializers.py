from rest_framework import serializers

from event.models import Event
from event.validators import validate_status


class EventSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    room_id = serializers.UUIDField(source='room_reservation_id')
    rpg_status = serializers.IntegerField(
        source='status',
        validators=[validate_status]
    )

    class Meta:
        model = Event
        fields = (
            'id',
            'hotel_id',
            'room_id',
            'timestamp',
            'rpg_status',
            'night_of_stay',
        )

    def create(self, validated_data):
        """
        This method is overriden to support upsert operation.
        """
        id = validated_data.pop('id')
        obj, _ = Event.objects.update_or_create(id=id, defaults=validated_data)

        return obj
