import django_filters
from django.db.models import Q
from django.forms import TextInput

from attribute.models import Attribute


class AttributeFilterset(django_filters.FilterSet):
    search = django_filters.CharFilter(
        method="filter_keyword",
        label="search",
        widget=TextInput(attrs={"placeholder": "code, class_id, etc..."}),
    )

    class Meta:
        model = Attribute
        fields = ["search"]

    def filter_keyword(self, queryset, name, value):
        if value.isdigit():
            return queryset.filter(
                Q(code__icontains=value) | Q(class_id__Code__icontains=value)
            )
        else:
            return queryset.filter(
                Q(target_name__icontains=value) | Q(source_name__icontains=value)
            )
