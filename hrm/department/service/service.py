"""Module with two classes for CRUD operations with Department and
Employee models instances respectively"""
import logging
from django.views.generic import ListView
from department.models.models import Department, Employee


logger = logging.getLogger(__name__)


class DepartmentsCustom(ListView):
    """Class for CRUD operation with Department model instances"""
    object_list = Department.objects.all().order_by('title')
    model = Department
    allow_empty = False

    def get(self, request, *args, **kwargs):
        if isinstance(request.resolver_match.kwargs.get('slug', None), str):
            self.object_list = Employee.objects.filter(department__slug=
                                                       request.resolver_match.kwargs.get('slug'))
            context = super().get_context_data(**kwargs)
            return context
        context = super().get_context_data(**kwargs)
        return context
