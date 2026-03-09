import pytest 
from rest_framework.test import APIClient
from university.models import Teacher, Department

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def department():
    return Department.objects.create(name = "Engineering")

@pytest.fixture
def teacher(department):
    return Teacher.objects.create(name="asad",department = department)



