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
        # 'icon'
        )
    inlines = [CategoryTranslationInline]
