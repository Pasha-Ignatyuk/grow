"""View is responsible for displaying information (visualization)"""
import logging
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from department.models.models import Department, Employee

logger = logging.getLogger(__name__)

class EmployeeDetailView(DetailView):
    """View for employee's information rendering"""
    def get(self, request, empl_id):
        """getting the employee's data"""
        employee = get_object_or_404(Employee, id=empl_id)
        return render(request, 'employee_detail.html', {'employee': employee})

class DepartmentCreateView(CreateView):
    """A base view for creating a new DEPARTMENT model instance"""
    model = Department
    fields = ['title',]
    template_name = 'add_new_dept.html'
    success_url = reverse_lazy('main_page')

class DepartmentUpdateView(UpdateView):
    """A base view for updating an existing DEPARTMENT model instance"""
    model = Department
    fields = ['title', ]
    template_name = 'add_new_dept.html'
    success_url = reverse_lazy('main_page')

class DepartmentListView(ListView):
    """A base view for displaying a list of Department model objects"""
    model = Department
    template_name = 'main_page.html'

class DepartmentDetailView(DetailView):
    """A base view for displaying a single department object"""
    def get(self, request, slug):
        """method for current department retrieving and rendering"""
        department = get_object_or_404(Department, slug=slug)
        employee = Employee.objects.filter(department__slug=slug).order_by('id')
        return render(request, 'department_detail.html', {'department': department,
                                                          'employee': employee})

class DepartmentDeleteView(DeleteView):
    """A base view for deleting department model instance"""
    model = Department
    template_name = 'dept_deletion.html'
    success_url = reverse_lazy('main_page')

class EmployeeSearchView(View):
    """View for searching employees of current department by date of birth"""

    def get(self, request, *args, **kwargs):
        """Searching employees with current date of birth"""
        if request.method == "GET":
            department_slug = request.GET.get('department_slug')
            startpoint = request.GET.get('startpoint')
            endpoint = request.GET.get('endpoint')
            selection = Employee.objects.filter(department__slug=department_slug,
                                                birthday__gte=startpoint,
                                                birthday__lte=endpoint)
            return render(request, 'search.html', {'selection': selection})
        return None
