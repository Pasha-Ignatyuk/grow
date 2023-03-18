"""View is responsible for displaying information (visualization)"""
import json
import logging
from django.views import View
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.http import QueryDict
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from department.models.models import Department, Employee
from department.forms.forms import DeptForm
from department.service.draft_service import DepartmentService, EmployeeService
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


logger = logging.getLogger(__name__)

class DepartmentCreateView(DepartmentService, CreateView):
    template_name = 'add_new_dept.html'


class DepartmentUpdateView(DepartmentCreateView, UpdateView):
    pass


class DepartmentListView(DepartmentService, ListView):
    template_name = 'main_page.html'


class DepartmentDetailView(DepartmentService, EmployeeService, DetailView):
    template_name = 'department_detail.html'


class DepartmentDeleteView(DepartmentService, DeleteView):
    template_name = 'dept_deletion.html'


class EmployeeDetailView(EmployeeService, DetailView):
    template_name = 'employee_detail.html'


# class DepartmentsList(View):
#     """Presents a list of all departments on web page"""
#
#     # @staticmethod
#     # def get(request):
#     #     """Uses getting_department method from DepartmentService class
#     #     to retrieve all departments from DB"""
#     #     return render(request, 'main_page.html', {'departments': DepartmentService.getting_department()})
#
#     @staticmethod
#     def get(*args, **kwargs):
#         """Uses getting_department method from DepartmentService class
#         to retrieve all departments from DB"""
#         return render(*args, **kwargs)
#
#
# class AddNewDept:
#     """Form for adding a new department"""
#
#     # @staticmethod
#     # def dispatch(request):
#     #     """Renders form for CREATING a new department"""
#     #     if request.method == "POST":
#     #         print(request.body.decode('utf-8'))
#     #         # qd = dict(QueryDict.iteritems())
#     #         # print(qd)
#     #         print(request.POST.keys())
#     #         department = Department()
#     #         department.title = request.POST.get("title")
#     #         department.save()
#     #         return render(request, 'main_page.html')
#     #     return render(request, 'add_new_dept.html')
#
#     @staticmethod
#     def dispatch(*args, **kwargs):
#         # if request.method == "POST":
#         #     departments = DepartmentService.dispatch(request)
#         #     return render(request, 'main_page.html', {'departments': departments})
#         return render(*args, **kwargs)
#
#
# class DepartmentDeleteView(DeleteView):
#
#     @staticmethod
#     def get(*args, **kwargs):
#         # department = Department.objects.get(slug=slug)
#         # department.delete()
#         return render(*args, **kwargs)
#
#
# class DepartmentDetail(View):
#     """View for a specific department page. Accepts department's ID """
#
#     # @staticmethod
#     # def get(request, slug):
#     #     """Uses getting_employee method from EmployeeService class and getting_department
#     #     from DepartmentService class to retrieve all employees of current dept from DB"""
#     #     return render(request, 'department_detail.html',
#     #                   {'department': DepartmentService.getting_department(slug=slug).values()[0],
#     #                    'employee': EmployeeService.getting_employee(
#     #                        department__slug=slug)})
#     @staticmethod
#     def get(*args, **kwargs):
#         """Uses getting_employee method from EmployeeService class and getting_department
#         from DepartmentService class to retrieve all employees of current dept from DB"""
#         return render(*args, **kwargs)
#
#
# class EmployeeDetail(View):
#     """View for a specific employee page. Accepts employee's ID """
#
#     @staticmethod
#     def get(*args, **kwargs):
#         """Uses getting_employee method from EmployeeService class to retrieve all
#         employees's data"""
#         return render(*args, **kwargs)