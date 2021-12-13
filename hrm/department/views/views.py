"""View - is responsible for displaying information (visualization)"""
import logging
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from department.models.models import Department, Employee
from department.forms.forms import DeptForm


logger = logging.getLogger(__name__)


def departments_list(request):
    """Presents a list of all departments on web page"""
    departments = Department.objects.all().order_by('title')
    return render(request, 'main_page.html', {'departments': departments})


def add_new_dept(request):
    """Form for adding a new department"""
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            dept = form.save(commit=False)
            dept.author = request.user
            dept.save()
            departments = Department.objects.all().order_by('title')
            return render(request, 'main_page.html', {'departments': departments})
    else:
        form = DeptForm()
    return render(request, 'add_new_dept.html', {'form': form})


class DepartmentUpdateView(UpdateView):
    """A view for department updating"""
    model = Department
    form_class = DeptForm
    template_name = 'add_new_dept.html'


class DepartmentDeleteView(DeleteView):
    """A view that displays a confirmation page and deletes an existing department"""
    model = Department
    success_url = reverse_lazy('main_page')
    template_name = 'dept_deletion.html'


def department_detail(request, prime_key):
    """View for a specific department page. Accepts department's ID """
    department = get_object_or_404(Department, id=prime_key)
    employee = Employee.objects.filter(department__id=prime_key)
    return render(request, 'department_detail.html', {'department': department,
                                                      'employee': employee})


def employee_detail(request, empl_id):
    """View for a specific employee page. Accepts employee's ID """
    employee = get_object_or_404(Employee, id=empl_id)
    return render(request, 'employee_detail.html', {'employee': employee})
