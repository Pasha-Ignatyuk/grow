"""APIViews for API endpoints"""
from django.core.cache import cache
from rest_framework.generics import ListAPIView,  CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from department.models.models import Department, Employee
from department.rest.serializers import DepartmentSerializer, EmployeeSerializer


class DepartmentPagination(LimitOffsetPagination):
    """Pagination determine the structure of Department model instances responses"""
    default_limit = 10
    max_limit = 100

class EmployeePagination(LimitOffsetPagination):
    """Pagination determine the structure of Employee model instances responses"""
    default_limit = 10
    max_limit = 100

class DepartmentView(ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView):
    """CRUD methods for Department model"""
    queryset = Department.objects.all().order_by('title')
    serializer_class = DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = DepartmentPagination
    lookup_field = 'id'

    def list(self, request, *args, **kwargs):
        if isinstance(request.resolver_match.kwargs.get('id', None), int):
            return super().retrieve(request, *args, **kwargs)
        return super().list(request)

    def create(self, request, *args, **kwargs):
        title = request.data.get('title')
        if title is None:
            raise ValidationError({'title': 'Must not be empty'})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == 200:
            department = response.data
            department_id = department['id']
            cache.set(f'department_data_{department_id}', {
                'title': department['title'],
                'slug': department['slug'],
            })
        return response

    def delete(self, request, *args, **kwargs):
        department_id = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == 204:
            cache.delete(f'department_data_{department_id}')
        return response


class EmployeeView(ListAPIView):
    """CRUD methods for Employee model"""
    queryset = Employee.objects.all().order_by('surname')
    serializer_class = EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('department',)
    pagination_class = EmployeePagination
