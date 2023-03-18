"""Module for CRUD operations with database"""

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView
from department.forms.forms import DeptForm
from department.models.models import Department, Employee
# from department.views.views import AddNewDept, DepartmentsList, \
#     DepartmentDetail, EmployeeDetail, DepartmentDeleteView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin, BaseListView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from braces.views import SelectRelatedMixin


# class OwnerMixin(object):
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(owner=self.request.user)


# class OwnerEditMixin(object):
#     def form_valid(self, form):
#         form.instance.owner = self.request.user
#         return super().form_valid(form)
class EmployeeService(ListView, DetailView, CreateView, UpdateView, DeleteView):
    model = Employee
    select_related = ['department']


class DepartmentService(EmployeeService, ListView, DetailView, CreateView, UpdateView, DeleteView):
    model = Department
    # fields = ['title']
    success_url = reverse_lazy('main_page')
    form_class = DeptForm
    slug = model.slug
    object = None

    # def get_object(self, queryset=None):
    #     super().get_object()
    #     context = super().get_context_data()
    #     context['employee'] = Employee.objects.filter(department__slug=DepartmentService.slug)
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.all()

    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context['employee'] = Employee.objects.filter(department__slug=DepartmentService.slug)
    #     return context

    def delete(self):
        return super().delete()


# class DepartmentService(BaseListView, MultipleObjectMixin):
#     """Class for CRUD operations with Department model"""

    # @classmethod
    # def getting_department(cls, **kwargs):
    #     """Method for RETRIEVE information from Department model"""
    #     if kwargs:
    #         department = Department.objects.filter(**kwargs)
    #         return department
    #     return Department.objects.all().order_by('title')
    # @classmethod
    # def getting_department(cls, request, **kwargs):
    #     """Method for RETRIEVE information from Department model"""
    #     if kwargs:
    #         department = Department.objects.get(**kwargs)
    #         employees = Employee.objects.filter(department__slug=department.slug)
    #         return DepartmentsList.get(request, 'department_detail.html', {'department': department,
    #                                                                        'employees': employees})
    #     departments = Department.objects.all().order_by('title')
    #     return DepartmentsList.get(request, 'main_page.html', {'departments': departments})
    #
    # @classmethod
    # def deleting_department(cls, request, **kwargs):
    #     """Method for RETRIEVE information from Department model"""
    #     if kwargs:
    #         department = Department.objects.get(**kwargs)
    #         department.delete()
    #         departments = Department.objects.all().order_by('title')
    #         return DepartmentDeleteView.get(request, 'main_page.html', {'departments': departments})

    # @classmethod
    # def deleting_department(cls, request, **kwargs):
    #     """Method for RETRIEVE information from Department model"""
    #     if kwargs:
    #         department = Department.objects.get(**kwargs)
    #         return DepartmentDeleteView.get(request, 'dept_deletion.html')

    # @classmethod
    # def dispatch(cls, request, *args, **kwargs):
    #     """Renders form for CREATING a new department"""
    #     if request.method == "POST":
    #         # department = Department()
    #         # department.title = request.POST.get("title")
    #         # department.save
    #         form = DeptForm(request.POST)
    #         if form.is_valid():
    #             dept = form.save(commit=False)
    #             dept.save()
    #             departments = Department.objects.all().order_by('title')
    #         return AddNewDept.dispatch(request, 'main_page.html', {'departments': departments})
    #     else:
    #         form = DeptForm()
    #     return AddNewDept.dispatch(request, 'add_new_dept.html', {'form': form})
    #
    # @classmethod
    # def update(cls, request, **kwargs):
    #     """Renders form for UPDATING the department"""
    #     department = Department.objects.get(**kwargs)
    #     if request.method == "POST":
    #         form = DeptForm(request.POST, instance=department)
    #         if form.is_valid():
    #             department = form.save(commit=False)
    #             department.save()
    #             departments = Department.objects.all().order_by('title')
    #             return AddNewDept.dispatch(request, 'main_page.html', {'departments': departments})
    #     else:
    #         form = DeptForm(instance=department)
    #     return AddNewDept.dispatch(request, 'add_new_dept.html', {'form': form})


# class EmployeeService(object):
#     """Class for CRUD operations with Employee model"""
    # @classmethod
    # def getting_employee(cls, **kwargs):
    #     """Method for RETRIEVE information from Employee model"""
    #     if kwargs:
    #         return Employee.objects.filter(**kwargs)
    #     return Employee.objects.all().order_by('surname')
    # @classmethod
    # def getting_employee(cls, request, **kwargs):
    #     """Method for RETRIEVE information from Employee model"""
        # if request.method == "POST":
        #     context = super().get_context_data(**kwargs)
        #     # department_slug = request.POST.get('department_slug')
        #     # startpoint = request.POST.get('startpoint')
        #     # endpoint = request.POST.get('endpoint')
        #     department_slug = context.get('department_slug')
        #     startpoint = context.get('startpoint')
        #     endpoint = context.get('endpoint')
        #     selection = Employee.objects.filter(department__slug=department_slug,
        #                                         birthday__gte=startpoint,
        #                                         birthday__lte=endpoint)
        #     # import pdb;
        #     # pdb.set_trace()
        #     return EmployeeDetail.get(request, 'search_result.html', {'selection': selection})

        # if kwargs:
        #     employee = Employee.objects.get(**kwargs)
        #     # employee = Employee.objects.get(id=employee.id)
        #     return EmployeeDetail.get(request, 'employee_detail.html', {'employee': employee})
        # employees = Employee.objects.all().order_by('surname')
        # return EmployeeDetail.get(request, 'employee_detail.html', {'employees': employees})
