"""Model declaration"""
import logging
from django.db import models
from django.db.models import Avg
from django.urls import reverse_lazy
from django.utils.text import slugify

logger = logging.getLogger(__name__)


class Department(models.Model):
    """This is the department model"""
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, verbose_name='Slug')

    def __str__(self):
        """string representation of a Department class object """
        return f'{self.title}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @staticmethod
    def get_absolute_url():
        """returns the edited page of department"""
        return reverse_lazy('main_page')

    @property
    def average_salary(self):
        """Method of department's average salary, using aggregate queries"""
        average_salary = Employee.objects.filter(department=self).aggregate(Avg('salary'))
        if average_salary['salary__avg'] is None:
            return 'not applicable'
        return round(average_salary['salary__avg'], 2)


class Employee(models.Model):
    """This is the employee model"""
    id = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthday = models.DateField()
    salary = models.DecimalField(max_digits=7, decimal_places=2)
    slug = models.SlugField(max_length=200, verbose_name='Slug')

    def __str__(self):
        """string representation of an Employee class object """
        return f'{self.name} {self.surname} salary {self.salary}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + self.surname + self.birthday)
        super().save(*args, **kwargs)
