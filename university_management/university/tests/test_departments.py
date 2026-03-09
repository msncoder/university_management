import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from university.models import *

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def department(db):
    return Department.objects.create(name='physics')

@pytest.fixture
def list_url():
    return reverse("department-list")


@pytest.fixture
def detail_url(department):
    return lambda pk: reverse('department-detail',args=[pk])

@pytest.mark.django_db
def test_get_department_list(api_client,list_url,department):
    response = api_client.get(list_url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) > 0

def test_get_deparment_detail(api_client,department,detail_url):
    response = api_client.get(detail_url(department.id))
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == "physics"

@pytest.mark.django_db
def test_create_department(api_client,list_url):
    data = {'name':'mathematics'}
    response = api_client.post(list_url,data,format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Department.objects.filter(name='mathematics').exists()

@pytest.mark.django_db
def test_update_department(api_client,department,detail_url):
    data = {'name':'urdu'}
    response = api_client.put(detail_url(department.id),data,format='json')
    assert response.status_code == status.HTTP_200_OK
    department.refresh_from_db()
    assert department.name == "urdu"

@pytest.mark.django_db
def test_patial_update_department(api_client,department,detail_url):
    data = {'name':'chemistry'}
    response = api_client.patch(detail_url(department.id),data,format='json')
    assert response.status_code == status.HTTP_200_OK
    department.refresh_from_db()
    assert department.name == "chemistry"

@pytest.mark.django_db
def test_delete_department(api_client,department,detail_url):
    response = api_client.delete(detail_url(department.id))
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Department.objects.filter(id = department.id).exists()