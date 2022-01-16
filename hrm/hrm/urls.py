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
from django.urls import path
from department.rest.my_api_views import DepartmentView, EmployeeView
from department.views.views import DepartmentsCustomView
# from department.views.views import DepartmentsList

urlpatterns = [
    path('api', DepartmentView.as_view()),
    path('api/new', DepartmentView().as_view()),
    path('api/update', DepartmentView().as_view()),
    path('api/<int:id>', DepartmentView.as_view()),
    path('api/empl', EmployeeView.as_view()),

    path('admin/', admin.site.urls),
    path('', DepartmentsCustomView.as_view(), name='main_page'),
    path('<int:id>', DepartmentsCustomView.as_view(), name='department_detail'),
    path('new', DepartmentsCustomView.as_view(), name='add_new_dept'),
]
