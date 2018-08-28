from django.contrib import admin

from .models import Category, Image

def set_category_to_abstract(model_admin, request, queryset):
    queryset.update(category=Category.objects.get(name="Abstract"))

def set_category_to_flowers(model_admin, request, queryset):
    queryset.update(category=Category.objects.get(name="Flowers"))

def set_category_to_around_the_world(model_admin, request, queryset):
    queryset.update(category=Category.objects.get(name="Around the World"))

def set_category_to_other(model_admin, request, queryset):
    queryset.update(category=Category.objects.get(name="Other"))

class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'category')
    actions = [
        set_category_to_abstract,
        set_category_to_flowers,
        set_category_to_around_the_world,
        set_category_to_other
    ]

admin.site.register(Image, ImageAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')

admin.site.register(Category, CategoryAdmin)

