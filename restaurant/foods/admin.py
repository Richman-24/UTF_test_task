from django.contrib import admin

from foods.models import Food, FoodCategory


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "name_en", "name_ch", "order_id"]
    list_editable = ["order_id"]


@admin.register(Food)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name_ru", "cost", "is_special", "is_publish"]
    list_editable = ["is_publish", "is_special"]

