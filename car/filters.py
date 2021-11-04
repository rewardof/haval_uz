from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet, CharFilter
from car.models import Position


def split_string(string):
    list_values = string.split(',')
    list_values = [item.strip() for item in list_values]
    return list_values


class CarsPositionFilter(FilterSet):
    position_category = CharFilter(method='get_position_category')
    dealers = CharFilter(method='get_dealers')
    min_price = NumberFilter(field_name='min_price', lookup_expr='gt', label='price is greater than')
    max_price = NumberFilter(field_name='min_price', lookup_expr='lt', label='price is less than')
    transmission_type = CharFilter(field_name='transmission_name', lookup_expr='icontains', label='Transmission Type')
    wheel_drive_type = CharFilter(field_name='wheel_drive_name', lookup_expr='icontains', label='Wheel Drive Type')
    fuel_type = CharFilter(method='get_fuel_type', label='Fuel Type')
    engine_displacement_min = NumberFilter(field_name='engine_displacement', lookup_expr='gt',
                                           label='engine_displacement is greater than')
    engine_displacement_max = NumberFilter(field_name='engine_displacement', lookup_expr='lt',
                                           label='engine_displacement is less than')
    engine_power_min = NumberFilter(field_name='engine_power', lookup_expr='gt', label='engine_power is greater than')
    engine_power_max = NumberFilter(field_name='engine_power', lookup_expr='lt', label='engine_power is less than')
    color = CharFilter(method='get_color', label='Color')

    class Meta:
        model = Position
        fields = ('position_category', 'min_price', 'max_price', 'transmission_type', 'wheel_drive_type', 'fuel_type',
                  'engine_displacement_min', 'engine_displacement_max', 'engine_power_min', 'engine_power_max')

    def get_position_category(self, queryset, name, value):
        if value:
            lt = split_string(value)
            return queryset.filter(position_category__pk__in=lt)
        else:
            return queryset

    def get_dealers(self, queryset, name, value):
        if value:
            lt = split_string(value)
            return queryset.filter(dealers__pk__in=lt)
        else:
            return queryset

    def get_fuel_type(self, queryset, name, value):
        if value:
            lt = split_string(value)
            lt = [string.lower() for string in lt]
            return queryset.filter(fuel_type_name__in=lt)
        else:
            return queryset

    def get_color(self, queryset, name, value):
        if value:
            lt = split_string(value)
            queryset = Position.objects.filter(position_category__images_for_positioncategory__colored_images__color_title__in=lt)
            return queryset
        else:
            return queryset
