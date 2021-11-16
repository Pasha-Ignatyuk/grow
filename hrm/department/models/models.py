"""Model declaration"""
from django.db import models


class Department(models.Model):
    """This is the department model"""
    title = models.CharField(max_length=50)

    def __str__(self):
        """string representation of an Department class object """
        return f'{self.title}'


class Employee(models.Model):
    """This is the employee model"""
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        """string representation of an Employee class object """
        return f'{self.name} {self.surname} salary {self.salary}'
