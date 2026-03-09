import pytest 
from rest_framework.test import APIClient
from university.models import Teacher, Department

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def department():
    return Department.objects.create(name="Engineering")

@pytest.fixture
def teacher(department):
    return Teacher.objects.create(name="asad",department = department)

@pytest.mark.django_db
def test_create_teacher(api_client,department):
    url = "/api/teachers/"
    payload = {
        "name":"New Teacher",
        "department":department.id
    }

    response = api_client.post(url,payload,format='json')

    assert response.status_code == 201
    assert Teacher.objects.count() == 1
    assert response.data["name"] == "New Teacher"


@pytest.mark.django_db
def test_list_teacher(api_client,teacher):
    url = "/api/teachers/"
    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 1
    # assert response.data[0]['name'] == teacher.name


@pytest.mark.django_db
def test_retrieve_teacher(api_client,teacher):
    url = f'/api/teachers/{teacher.id}/'

    response = api_client.get(url)

    assert response.status_code == 200
    assert response.data["name"] == teacher.name


@pytest.mark.django_db
def test_update_teacher(api_client, teacher, department):
    url = f"/api/teachers/{teacher.id}/"

    payload = {
        "name": "Updated Name",
        "department": department.id
    }

    response = api_client.put(url, payload, format="json")

    teacher.refresh_from_db()

    assert response.status_code == 200
    assert teacher.name == "Updated Name"

        
@pytest.mark.django_db
def test_delete_teacher(api_client, teacher):
    url = f"/api/teachers/{teacher.id}/"

    response = api_client.delete(url)

    assert response.status_code == 204
    assert Teacher.objects.count() == 0