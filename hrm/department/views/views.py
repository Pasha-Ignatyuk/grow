"""View is responsible for displaying information (visualization)"""
import logging
import re
from django.template.loader import get_template
from django.http import HttpResponseRedirect, HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView, FormView, DetailView, RedirectView, TemplateView
from department.models.models import Department, Employee
from department.forms.forms import DeptForm
# from department.service.service import DepartmentsCustom
from django.views.generic.edit import DeletionMixin, DeleteView
# from department.service.utils import CustomTemplateMixin

logger = logging.getLogger(__name__)


# class DepartmentsCustomView(ListView, DetailView, DeleteView, CreateView):
#     """Class for CRUD operations with Department model instances in web-application"""
#     # object_list = Department.objects.all().order_by('title')
#     # slug_list = [item.slug for item in Department.objects.all()]
#     # model = Department
#     # allow_empty = False
#     # form_class = DeptForm
#     # # initial = {}
#     # # success_url = reverse_lazy('main_page')
#     # success_url = 'main_page'
#     # # templates_names = ['main_page.html', 'department_detail.html', 'dept_deletion.html', 'add_new_dept.html', 'add_new_dept.html']
#     # object = None
#     # # url = None
#     # # pattern_name = 'main_page'
#     # # query_string = False
#     # # permanent = False

#     def get(self, request, *args, **kwargs):
#         # if re.match('/[0-9]+/delete', request.get_full_path()):
#         #     return render(request, 'dept_deletion.html')
#         # elif re.match('/[0-9]+/update', request.get_full_path()):
#         #     pk = request.resolver_match.kwargs.get('pk')
#         #     obj = get_object_or_404(Department, pk=pk)
#         #     form = self.form_class(instance=obj)
#         #     return render(request, 'add_new_dept.html', {'form': form})
#         # elif re.match('/[0-9]+', request.get_full_path()):
#         #     self.object_list = Employee.objects.filter(department__id=
#         #                                                request.resolver_match.kwargs.get('pk'))
#         #     context = super().get_context_data(**kwargs)
#         #     return render(request, 'department_detail.html', context)
#         # elif re.match('/post', request.get_full_path()):
#         #     a = request.get_full_path()
#         #     print(a, request.resolver_match.kwargs, request.method)
#         #     form = self.form_class(initial=self.initial)
#         #     return render(request, 'add_new_dept.html', {'form': form})
#         # else:
#         #     context = super().get_context_data(**kwargs)
#         #     return render(request, 'main_page.html', context)
#
#         # if re.match('/[a-zA-Z]', request.get_full_path()):
#         #     self.object_list = Employee.objects.filter(department__slug=request.resolver_match.kwargs.get('slug'))
#         #     print(request.get_full_path())
#         #     context = super().get_context_data()
#         #     return render(request, super().get_template_names(), context)
#         # elif re.match('/post', request.get_full_path()):
#         #     form = self.form_class(initial=self.initial)
#         #     return render(request, 'department_form.html', {'form': form})
#         # print(dir(DepartmentsCustomView))
#         # super().get(request, *args, **kwargs)
#         # context = super().get_context_data(**kwargs)
#         # print(request.get_full_path())
#         # return render(request, super().get_template_names(), context)
#         context = super().get_context_data(**kwargs)
#         context['employees'] = Employee.objects.filter(department__id=
#                                                        request.resolver_match.kwargs.get('id'))
#         return render(request, super().get_template_names(), context)
#
#     def delete(self, request, *args, **kwargs):
#         pk = self.kwargs.get('pk')
#         if pk is not None:
#             obj = get_object_or_404(self.model, id=pk)
#             obj.delete()
#         #return HttpResponseRedirect(self.get_success_url())
#         return super().get_context_data(**kwargs)
#         # super().get_success_url()
#         # self.object = Department.objects.get(**kwargs)
#         # a = getattr(self.object, 'success_url')
#         # super().delete(request, *args, **kwargs)
#         # setattr(self, 'success_url', 'main_page')
#         # setattr(self, 'template_name', 'main_page')
#
#         # return HttpResponseRedirect(reverse('main_page'))
#         # content = super().get_context_data(**kwargs)
#         # response = request.write(content)
#         # return HttpResponseRedirect('')
#
#         # context = super().get_context_data(**kwargs)
#         # return HttpResponseRedirect(reverse('main_page'))
#
#         # self.object_list = Department.objects.all().order_by('title')
#         # content = self.object_list
#         # return render(request, 'main_page.html', {'content': content})
#
#         # return HttpResponseRedirect(reverse_lazy('main_page'))  # 1.
#         # return redirect('main_page', permanent=True)  # 2.
#         # return HttpResponseRedirect(self.get_success_url())  # 3.
#         # return HttpResponseRedirect(self.success_url)  #4.
#         # context = super().get_context_data(**kwargs)  # 5.
#         # return render(request, 'main_page.html', context)  # 5.
#         # return redirect('/')  # 6.
#         # return HttpResponseRedirect(Department.get_absolute_url())
#         # return get_template('main_page.html')
#         # self.object = Department.objects.get(**kwargs)
#
#         # self.object.delete()
#         # context = super().get_context_data()
#         # return render(request, 'main_page.html', context)
#
#
#
#     # def post(self, request, *args, **kwargs):
#         # if request.method == 'POST':
#         #     form = DeptForm(request.POST)
#         #     if form.is_valid():
#         #         dept = form.save(commit=True)
#         #         dept.save()
#         #         context = super().get_context_data()
#         #         return render(request, 'main_page.html', context)
#         # return render(request, 'add_new_dept.html', {'form': form})
#
#         # super().post(request, *args, **kwargs)
#         # context = super().get_context_data(**kwargs)
#         # return render(request, super().get_template_names(), context)
#         # return HttpResponseRedirect('main_page')
#
#     # def put(self, request, *args, **kwargs):
#     #     pk = self.kwargs.get('pk')
#     #     obj = get_object_or_404(self.model, pk=pk)
#     #     if request.method == "POST":
#     #         form = DeptForm(request.POST, instance=obj)
#     #         # if form.is_valid():
#     #         #     # obj = form.save(commit=False)
#     #         #     form.save()
#     #         #     context = super().get_context_data(**kwargs)
#     #         #     return render(request, 'main_page.html', context)
#     #         super().put(request, pk=pk, *args, **kwargs)
#     #     return render(request, 'add_new_dept.html', {'form': form})
#     #     self.post(request, *args, **kwargs)
#
# # class DepartmentsList(DepartmentsCustom):
# #
# #     def get(self, request):
# #         context = super().get(request)
# #         return render(request, 'main_page.html', context)
