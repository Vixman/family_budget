from django.test import TestCase
from rest_framework import status


class TestBase(TestCase):
    def assert_200_status_code(self, status_code):
        self.assertEqual(status_code, status.HTTP_200_OK)

    def assert_404_status_code(self, status_code):
        self.assertEqual(status_code, status.HTTP_404_NOT_FOUND)

    def assert_400_status_code(self, status_code):
        self.assertEqual(status_code, status.HTTP_400_BAD_REQUEST)

    def assert_not_empty_list_view_results(self, data):
        self.assertTrue(len(dict(data)["results"]) > 0)

    def assert_response_detailed_view_keys(self, data, expected_keys):
        self.assertEqual(set(dict(data).keys()), set(expected_keys))

    def assert_response_list_view_keys(self, data, expected_keys):
        self.assertEqual(set(dict(data)["results"][0].keys()), set(expected_keys))
