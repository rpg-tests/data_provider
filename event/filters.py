from django_filters import rest_framework as filters


from event.models import Event


class EventFilter(filters.FilterSet):
    hotel_id = filters.NumberFilter(field_name='hotel_id')
    room_id = filters.UUIDFilter(field_name='room_reservation_id')

    updated__gte = filters.DateTimeFilter(
        field_name='timestamp',
        lookup_expr='gte'
    )
    updated__lte = filters.DateTimeFilter(
        field_name='timestamp',
        lookup_expr='lte'
    )

    night_of_stay__gte = filters.DateFilter(
        field_name='night_of_stay',
        lookup_expr='gte'
    )
    night_of_stay__lte = filters.DateFilter(
        field_name='night_of_stay',
        lookup_expr='lte'
    )

    rpg_status = filters.NumberFilter(field_name='status')

    class Meta:
        model = Event
        fields = (
            'id',
            'hotel_id',
            'room_id',
            'rpg_status',
            'night_of_stay',
        )
