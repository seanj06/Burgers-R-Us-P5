from django.contrib import admin
from .models import Food, Category, SubCategory

# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'sub_category',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )    


admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
