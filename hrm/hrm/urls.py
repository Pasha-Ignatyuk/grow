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
from department.views.views import departments_list, department_detail, employee_detail, DepartmentUpdateView, \
    DepartmentDeleteView, add_new_dept

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', departments_list, name='main_page'),
    path('<int:pk>', department_detail, name='department_detail'),
    path('<int:pk>/edit', DepartmentUpdateView.as_view(), name='add_new_dept'),
    path('<int:pk>/delete', DepartmentDeleteView.as_view(), name='dept_deletion'),
    path('department/<int:empl_id>', employee_detail, name='employee_detail'),
    path('new', add_new_dept, name='add_new_dept'),
]
