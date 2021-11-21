"""Module for registration of models"""
from django.contrib import admin
from department.models.models import Department, Employee

admin.site.register(Department)
admin.site.register(Employee)
