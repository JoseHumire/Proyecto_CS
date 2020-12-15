import django_filters

from django_filters import CharFilter

from .models import *


class ProfessionalFilter(django_filters.FilterSet):
    user__first_name = CharFilter(lookup_expr='icontains')
    user__last_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Professional
        fields = ['city', 'professions']
