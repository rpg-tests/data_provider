from rest_framework import status
from rest_framework.test import APITestCase


class TestEventEndpoint(APITestCase):

    def setUp(self):
        self.url = '/events/'

    def test_get(self):
        response = self.client.get(self.url)

        self.assertNotEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_post(self):
        response = self.client.post(self.url)

        self.assertNotEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_put(self):
        response = self.client.put(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def test_delete(self):
        response = self.client.delete(self.url)

        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED
        )
