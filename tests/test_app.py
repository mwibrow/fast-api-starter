"""
Tests for the app module.
"""

import unittest
from starlette.testclient import TestClient


from app.app import get_app


class TestApp(unittest.TestCase):
    """Basic example tests."""

    def setUp(self):
        """Set up tests"""
        self.client = TestClient(get_app())

    def test_status(self):
        """Test status"""
        response = self.client.get('/')
        assert response.status_code == 200
