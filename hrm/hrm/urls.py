"""hrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import uuid
from django.contrib import admin
from django.urls import path, reverse_lazy
from department.rest.my_api_views import DepartmentView, EmployeeView
# from department.views.views import DepartmentsCustomView
# from department.views.views import DepartmentsList
from department.views.draft_view import DepartmentListView, DepartmentDetailView, DepartmentCreateView, \
    DepartmentUpdateView, DepartmentDeleteView, EmployeeDetailView

urlpatterns = [
    path('get/departments', DepartmentView.as_view()),
    path('api/new', DepartmentView().as_view()),
    path('api/update', DepartmentView().as_view()),
    path('api/<int:id>', DepartmentView.as_view()),
    path('api/empl', EmployeeView.as_view()),

    path('admin/', admin.site.urls),

    # path('', DepartmentsCustomView.as_view(), name='department_list'),
    # path('post', DepartmentsCustomView.as_view(),
    #      name='department_form'),
    # path('<slug:slug>', DepartmentsCustomView.as_view(), name='department_detail'),
    # path('<slug:slug>/delete', DepartmentsCustomView.as_view(), name='department_confirm_delete'),
    # path('<slug:slug>/update', DepartmentsCustomView.as_view(), name='department_form'),

    # path('', DepartmentsCustomView.as_view(template_name='main_page.html'), name='main_page'),
    # path('<int:pk>', DepartmentsCustomView.as_view(template_name='department_detail.html'), name='department_detail'),
    # path('<int:pk>/delete', DepartmentsCustomView.as_view(template_name='dept_deletion.html'), name='dept_deletion'),
    # path('post', DepartmentsCustomView.as_view(template_name='add_new_dept.html'), name='add_new_dept'),
    # path('<int:pk>/update', DepartmentsCustomView.as_view(template_name='add_new_dept.html'), name='add_new_dept'),

    path('', DepartmentListView.as_view()),
    path('<int:pk>', DepartmentDetailView.as_view(), name='department_detail'),
    path('<int:pk>/delete', DepartmentDeleteView.as_view(), name='dept_deletion'),
    path('post', DepartmentCreateView.as_view(), name='add_new_dept'),
    path('<int:pk>/update', DepartmentUpdateView.as_view(), name='add_new_dept'),
    path('department/<slug:slug>', EmployeeDetailView.as_view(), name='employee_detail'),
]
