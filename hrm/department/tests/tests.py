"""Module with Unit Tests"""
from decimal import Decimal
import datetime
from django.test import TestCase
from django.contrib.auth import get_user_model
from department.models.models import Department, Employee

User = get_user_model()


class HRMTestCase(TestCase):
    """Instances of the TestCase class represent the logical test units in the unittest universe.
    This class is intended to be used as a base class, with specific tests being implemented by
    concrete subclasses. This class implements the interface needed by the test runner to allow
    it to drive the tests, and methods that the test code can use to check for and report various
    kinds of failure."""
    def setUp(self):
        """Method called to prepare the test fixture. This is called immediately before calling
        the test method. Preliminary creation of objects of classes Department and Employee for
        subsequent testing"""
        self.user = User.objects.create(username='testuser')
        self.department = Department.objects.create(id=1, title="Test department")
        self.employee = Employee.objects.create(department=self.department,
                                                name="Konstantin", surname="Konstantinov",
                                                birthday=datetime.date(1982, 12, 14),
                                                salary=Decimal('10000.00'))
        self.employee = Employee.objects.create(department=self.department, name="Efim",
                                                surname="Efimov",
                                                birthday=datetime.date(1991, 6, 25),
                                                salary=Decimal('1000.00'))

    def test_average_salary(self):
        """Checking the calculation of the average salary of two employees of the department,
        named "Test department" """
        average_salary = self.department.average_salary
        self.assertEqual(average_salary, 5500.00)

    def test_department_str_method(self):
        """Checking that the __str__ method of Department model works properly"""
        self.assertEqual(self.department.__str__(), f'{self.department.title}')

    def test_employee_str_method(self):
        """Checking that the __str__ method of Employee model works properly"""
        self.assertEqual(self.employee.__str__(), str(self.employee))
