from django.urls import include, path

from api.foods.urls import foods_urls

app_name = 'api'

urlpatterns = [
    path('v1/foods/', include(foods_urls)),
]