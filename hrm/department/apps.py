"""A registry of installed applications that stores configuration and provides introspection"""
from django.apps import AppConfig


class DepartmentConfig(AppConfig):
    """The RmConfig.name attribute tells Django that this configuration applies to Rm application"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'department'
