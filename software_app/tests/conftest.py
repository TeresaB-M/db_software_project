import os
import sys
import pytest
sys.path.append(os.path.dirname(__file__))

# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'final_project.settings')
import django
# Import settings
django.setup()  # This needs to be done after you set the environ

from django.test import Client


@pytest.fixture
def client():
    """Create a customer object"""
    client = Client()
    return client
