"""View is responsible for displaying information (visualization)"""
import logging
from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from department.models.models import Department, Employee
from department.forms.forms import DeptForm
# from department.service.service import DepartmentsCustom

logger = logging.getLogger(__name__)


class DepartmentsCustomView(ListView, CreateView):
    """Class for CRUD operations with Department model instances in web-application"""
    object_list = Department.objects.all().order_by('title')
    model = Department
    allow_empty = False
    form_class = DeptForm
    success_url = reverse_lazy('main_page')

    def get(self, request, *args, **kwargs):
        if isinstance(request.resolver_match.kwargs.get('id', None), int):
            self.object_list = Employee.objects.filter(department__id=
                                                       request.resolver_match.kwargs.get('id'))
            context = super().get_context_data(**kwargs)
            return render(request, 'department_detail.html', context)
        context = super().get_context_data(**kwargs)
        return render(request, 'main_page.html', context)

    def post(self, request, *args, **kwargs):
        form = self.form_class()
        if request.method == 'POST':
            form = DeptForm(request.POST)
            if form.is_valid():
                dept = form.save(commit=True)
                dept.save()
                return HttpResponseRedirect(reverse('main_page'))
        return render(request, 'add_new_dept.html', {'form': form})

# class DepartmentsList(DepartmentsCustom):
#
#     def get(self, request):
#         context = super().get(request)
#         return render(request, 'main_page.html', context)
