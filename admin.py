from django.contrib import admin
from category import models


class CategoryTranslationInline(admin.StackedInline):
    """
        @description: JobCategoryInline
    """

    model = models.CategoryTranslation
    extra = 0

    fields = [
        'language',
        'name',
        'description',
    ]
    formfield_overrides = {

    }

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'interface'
        )
    inlines = [CategoryTranslationInline]


@admin.register(models.CategoryTranslation)
class CategoryTranslationAdmin(admin.ModelAdmin):
    list_display = (
        'language',
        'name',
        'description',
    )

@admin.register(models.CategoryRelatedTo)
class CategoryRelatedToAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'relatedModel',
        'relatedModelId',
    )
