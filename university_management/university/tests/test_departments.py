import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import *

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def department():
    return Department.objects.create(name='physics')

@pytest.fixture
def list_url():
    return reverse("api/departments/")


@pytest.fixture
def list_url():
    return reverse('department-list')

@pytest.fixture
def details_url(department):
    return lambda pk: reverse('department-detail',args=[pk])