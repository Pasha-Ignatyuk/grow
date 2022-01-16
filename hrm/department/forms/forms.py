"""User-filled forms"""
from django import forms
from department.models.models import Department


class DeptForm(forms.ModelForm):
    """Form for adding a new department"""
    class Meta:
        """Form fields to fill out """
        model = Department
        fields = ('title',)
