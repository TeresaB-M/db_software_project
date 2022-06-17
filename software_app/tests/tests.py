from django.test.utils import setup_test_environment
setup_test_environment()
from software_app. models import Software
import pytest


def test_details(client):
    """Send a request to the application whether it ended with the code 200"""

    response = client.get('/software/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_should_create_software():
    """Test verifying the creation of an element in the database"""

    softwares = Software.objects.all()
    software_before = sum(1 for software in softwares if software.name == "Adobe Photoshop") + 1
    Software.objects.create(name="Adobe Photoshop")
    softwares = Software.objects.all()
    software_after = sum(1 for software in softwares if software.name == "Adobe Photoshop")
    assert software_before == software_after


@pytest.mark.django_db
def test_update_software():
    """Test confirming the update in the database """

    softwares = Software.objects.create(name="Python3.8", description="wersja standard")
    assert softwares.pk is not None
    softwares.name = "Python"
    softwares.save()
    assert softwares.name == "Python"
