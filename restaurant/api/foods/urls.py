from django.urls import path

from api.foods.views import FoodListView

foods_urls = [
    path('', FoodListView.as_view()),
]