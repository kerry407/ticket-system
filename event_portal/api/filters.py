import django_filters
from ..models import Event

class EventFilter(django_filters.FilterSet):
    event_start_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Event 
        fields = ["event_start_date", "location", "host__email", "category__name"]