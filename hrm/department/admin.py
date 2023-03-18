"""Module for registration of models"""
from django.contrib import admin
from department.models.models import Department, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    """Designation of auto-filled Department model fields"""
    list_display = ['id', 'title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Designation of auto-filled  and displayed Employee model fields"""
    list_display = ['id', 'name', 'surname', 'salary']
    prepopulated_fields = {'slug': ('name', 'surname', 'birthday',)}
