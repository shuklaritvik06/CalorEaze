from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import CalorieModel
from authentication.models import DiveUser
from extras.models import ExpectedCalories


class CaloriesAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.create_url = '/api/v1/calories/daily/create/'
        self.update_url = '/api/v1/calories/daily/update/'
        self.delete_url = '/api/v1/calories/daily/delete/'
        self.filter_url = '/api/v1/calories/daily/filter/'
        self.user_id_filter = '/api/v1/calories/daily/own/'
        self.user = DiveUser.objects.create_superuser(password='password112!@@', email='testemail@gmail.com')
        self.client.force_authenticate(user=self.user)
        self.create_data = {
            "query": "2 slices of bread",
        }
        self.update_data = {
            "query": "2 plates rice",
        }
        ExpectedCalories.objects.create(expected=205.45, user_id=self.user)

    def test_create_calorie(self):
        response = self.client.post(self.create_url, self.create_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CalorieModel.objects.count(), 1)

    def test_get_calorie(self):
        calorie = CalorieModel.objects.create(query="2 slices of bread", total_calories=300.45, user_id=self.user)
        response = self.client.get(f"{self.filter_url}{calorie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(float(response.json()['message']['total_calories']), calorie.total_calories)

    def test_update_calorie(self):
        calorie = CalorieModel.objects.create(query="2 slices of bread", total_calories=300.45, user_id=self.user)
        response = self.client.put(f"{self.update_url}{calorie.id}/", self.update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_calorie(self):
        calorie = CalorieModel.objects.create(query="2 slices of bread", total_calories=300.45, user_id=self.user)
        response = self.client.delete(f"{self.delete_url}{calorie.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CalorieModel.objects.count(), 0)
