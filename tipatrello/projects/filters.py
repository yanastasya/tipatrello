import django_filters
from .models import Project
 
class ProjectFilter(django_filters.FilterSet):    
    is_active = django_filters.BooleanFilter()
    class Meta:
        model = Project
        fields = ['is_active',]