from django.urls import path

from event.views import EventListView

urlpatterns = [
    path('events/', EventListView.as_view(), name='events'),
]
