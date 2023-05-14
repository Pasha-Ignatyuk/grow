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
from django.contrib import admin
from django.urls import path
from department.rest.my_api_views import DepartmentView, EmployeeView
from department.views.views import DepartmentListView, DepartmentDetailView, DepartmentCreateView, \
    DepartmentUpdateView, DepartmentDeleteView, EmployeeDetailView, EmployeeSearchView


urlpatterns = [
    path('get/departments', DepartmentView.as_view()),
    path('api/new', DepartmentView().as_view()),
    path('api/update', DepartmentView().as_view()),
    path('api/<int:id>', DepartmentView.as_view()),
    path('api/empl', EmployeeView.as_view()),
    path('admin/', admin.site.urls),
    path('', DepartmentListView.as_view(), name='main_page'),
    path('<slug:slug>', DepartmentDetailView.as_view(), name='department_detail'),
    path('<search', EmployeeSearchView.as_view(), name='search'),
    path('<slug:slug>/delete', DepartmentDeleteView.as_view(), name='dept_deletion'),
    path('<slug:slug>/update', DepartmentUpdateView.as_view(), name='add_new_dept'),
    path('department/<int:empl_id>', EmployeeDetailView.as_view(), name='employee_detail'),
    path('post', DepartmentCreateView.as_view(), name='add_new_dept'),
]
