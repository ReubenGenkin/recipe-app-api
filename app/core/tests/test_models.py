"""
tests for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models"""

    def create_user_with_email_successful(self):

        email = 'test@example.com'
        password = 'testpass'
        user = get_user_model().objects.create.user(
            email=email,
            password=password
        )


