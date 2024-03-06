
from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.models.serialize import serializer__serialize__, serializer__init__
from django.forms.models import model_to_dict
from category.__rules__.stack import CATEGORY_RULESTACK

class CategoryTranslation(BaseMetadataModel):
    icon = models.ForeignKey(
        'mediacenter.Icon',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    language = models.CharField(
        'language',
        max_length=255,
        default='fr',
        choices=(
            ('fr', 'fr'),
        ),
    )

    name = models.CharField(
        max_length=255, 
    )

    description = models.TextField(blank=True, null=True)

    translateObject = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        # related_name='category_translates',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.language
    
    def serialize(self, request):
        """
            @description: 
        """
        serialize = model_to_dict(self)
        return serialize


class Category(BaseMetadataModel):
    translation_model = CategoryTranslation

    @serializer__init__
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    interface = models.CharField(
        max_length=255, 
        blank=True, 
        null=True,
        choices=CATEGORY_RULESTACK.models_choices(),
    )
    icon = models.ForeignKey(
        'mediacenter.Icon',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=255, 
        unique=True,
    )

    description = models.TextField(
        blank=True, 
        null=True
    )


    def __str__(self):
        return self.name

    @serializer__serialize__
    def serialize(self, request, **kwargs):
        """
            @description: 
        """
        serialize = model_to_dict(self)
        return serialize
    
class SelectedCategory(BaseMetadataModel):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.category.name

    @serializer__serialize__
    def serialize(self, request, **kwargs):
        """
            @description: 
        """
        serialize = model_to_dict(self)
        return serialize