"""Module to convert complex data such as querysets and model instances to native Python
datatypes that can then be easily rendered into JSON, XML or other content types"""
from rest_framework import serializers
from department.models.models import Department, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    """Class for representing information in JSON format"""
    class Meta:
        """Designation of model fields to display in JSON format"""
        model = Department
        fields = ('id', 'title', 'slug')

class EmployeeSerializer(serializers.ModelSerializer):
    """Class for representing information in JSON format"""
    class Meta:
        """Designation of model fields to display in JSON format"""
        model = Employee
        fields = ('id', 'name', 'surname', 'birthday', 'salary', 'slug')
