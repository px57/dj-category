
from django.db import models
from django.forms.models import model_to_dict
from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver

from kernel.models.base_metadata_model import BaseMetadataModel
from kernel.models.serialize import serializer__serialize__, serializer__init__
from kernel.models.fetch_all_models_file import choicesListRelatedModels

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
    
class CategoryRelatedTo(BaseMetadataModel):
    """
    Is the model that will be used to link a category to another model
    """

    @serializer__init__
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


    relatedModel = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        choices=choicesListRelatedModels()
    )

    # -> Get the nice object
    relatedModelId = models.IntegerField(
        null=True, 
        blank=True
    )

    interface = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        default=None,
        choices=CATEGORY_RULESTACK.models_choices()
    )

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
    

@receiver(pre_save, sender=CategoryRelatedTo)
def pre_save_categoryrelatedto(sender, instance, **kwargs):
    """
        @description: 
    """
    _in = CATEGORY_RULESTACK.get_interface(instance.interface)()
    _in.dbCategoryRelatedTo__pre_save(sender, instance, **kwargs)

@receiver(pre_delete, sender=CategoryRelatedTo)
def pre_delete_categoryrelatedto(sender, instance, **kwargs):
    """
        @description: 
    """
    _in = CATEGORY_RULESTACK.get_interface(instance.interface)()
    _in.dbCategoryRelatedTo__pre_delete(sender, instance, **kwargs)