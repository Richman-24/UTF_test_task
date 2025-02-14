from rest_framework.generics import ListAPIView
from django.db.models import Prefetch
from api.foods.serializers import FoodListSerializer
from foods.models import Food, FoodCategory


# Мне нравится так, когда логика на виду.
class FoodListView(ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(is_publish=True)

        categories = FoodCategory.objects.prefetch_related(
            Prefetch("food", queryset=published_foods)
        ).all()
        return categories


# Но можно написать кастомного менеджера и спрятать логику
class FoodListView(ListAPIView):
    queryset = FoodCategory.objects.with_published_foods()
    serializer_class = FoodListSerializer
