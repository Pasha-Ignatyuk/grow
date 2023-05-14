# """hrm URL Configuration
#
# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/3.1/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path
# from rest_framework.routers import SimpleRouter
# from department.models.models import Department, Employee
# from department.rest.my_api_views import DepartmentView, EmployeeView
# from department.views.views import DepartmentsList, DepartmentDetail, EmployeeDetail, DepartmentDeleteView, \
# AddNewDept
# from department.service.service import DepartmentService, EmployeeService
#
#
# urlpatterns = [
#     path('api', DepartmentView.as_view()),
#     path('api/new', DepartmentView().as_view()),
#     path('api/update', DepartmentView().as_view()),
#     path('api/<int:id>', DepartmentView.as_view()),
#     path('api/empl', EmployeeView.as_view()),
#
#     path('admin/', admin.site.urls),
#     # path('', DepartmentsList.as_view(), name='main_page'),
#     path('', DepartmentService.getting_department, name='main_page'),
#     # path('new', AddNewDept.as_view(), name='add_new_dept'),
#     path('new', DepartmentService.dispatch, name='add_new_dept'),
#     # path('new', get, name='add_new_dept'),
#     # path('<slug:slug>', DepartmentDetail.as_view(), name='department_detail'),
#     path('<slug:slug>', DepartmentService.getting_department, name='department_detail'),
#     path('search', EmployeeService.getting_employee, name='search_result'),
#     path('<slug:slug>/edit/', DepartmentService.update, name='add_new_dept'),
#     # path('<slug:slug>/delete/', DepartmentDeleteView.as_view(), name='dept_deletion'),
#     path('<slug:slug>/delete/', DepartmentService.deleting_department, name='dept_deletion'),
#     # path('department/<int:id>', EmployeeDetail.as_view(), name='employee_detail'),
#     path('department/<int:id>', EmployeeService.getting_employee, name='employee_detail'),
# ]
