from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import FoodCategory, Food

class FoodCategoryListViewTests(APITestCase):

    def setUp(self):
        # Создаем категорию и блюда
        self.category = FoodCategory.objects.create(
            name_ru='Напитки',
            order_id=10
        )
        self.food = Food.objects.create(
            category=self.category,
            code=1,
            internal_code=100,
            name_ru='Чай',
            description_ru='Чай 100 гр',
            cost='123.00',
            is_publish=True
        )

    def test_food_category_list(self):
        url = reverse('food-category-list')  # Имя URL-шаблона должно совпадать
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name_ru'], 'Напитки')
