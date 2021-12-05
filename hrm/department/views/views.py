"""View - is responsible for displaying information (visualization)"""
import logging
from django.shortcuts import render
from department.models.models import Department

logger = logging.getLogger(__name__)


def departments_list(request):
    """Presents a list of all departments on web page"""
    departments = Department.objects.all().order_by('title')
    return render(request, 'main_page.html', {'departments': departments})
