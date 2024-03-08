from django.shortcuts import render
from django.db.models import Q

from kernel.http import Response
from kernel.http import load_response
from kernel.i18n.models import translateDBQuerySet
from kernel.http.decorators import load_json
from kernel.interfaces.interfaces import message_addmethod_tointerface

from profiles.decorators import load_profile

from category.__rules__.stack import CATEGORY_RULESTACK
from category.models import Category, CategoryRelatedTo
from category.forms import SetSelectedCategoryForm


def res__Dbcategories(dbCategories, request, res=None):
    res.categories = [
        report.serialize(request)
        for report in translateDBQuerySet(
            request=request,
            querySet=dbCategories,
        )
    ]

@load_profile
@load_json
@load_response(stack=CATEGORY_RULESTACK)
def get_all(request, res=None):
    """
    Get all categories, to the user select one
    """
    _in = res.get_interface()
    dbCategories = Category.objects.filter(interface=_in.label)
    res__Dbcategories(dbCategories, request, res)
    return res.success()

@load_profile
@load_json
@load_response(stack=CATEGORY_RULESTACK)
def set_selected_category(request, res=None):
    _in = res.get_interface()
    form = SetSelectedCategoryForm({
        '_in': _in,
        'selected_list_id': request.POST.get('selected_list_id')
    })
    if not form.is_valid():
        return res.form_error(form)
    
    relatedModel = _in.relatedModel__for__set_selected_category()
    relatedModelId = _in.relatedModelId__for__set_selected_category()
    dbSelectedCategories = form.cleaned_data['selected_list_id']
    dbRelatedSelectedNow = CategoryRelatedTo.objects.filter(
        Q(interface=_in.label) &
        Q(relatedModelId=relatedModelId)
    ) 

    # -> Remove the unselected categories from the database
    for category in dbRelatedSelectedNow:
        if dbSelectedCategories.filter(id=category.category.id).exists():
            category.delete()

    # -> Add the selected categories to the database
    for category in dbSelectedCategories:
        if not dbRelatedSelectedNow.filter(category=category).exists():
            CategoryRelatedTo(
                category=category,
                interface=_in.label,
                relatedModel=relatedModel,
                relatedModelId=relatedModelId
            ).save()

    res__Dbcategories(dbSelectedCategories, request, res)
    return res.success()

@load_profile
@load_json
@load_response(stack=CATEGORY_RULESTACK)
def get_related_categories(request, res=None):
    """
    Get the related categories to the selected category
    """
    _in = res.get_interface()
    dbRelatedCategories = CategoryRelatedTo.objects.filter(
        Q(interface=_in.label) &
        Q(relatedModelId=_in.relatedModelId__for__get_related_categories())
    )
    # res__Dbcategories(dbRelatedCategories, request, res)
    related_categories = [category.category for category in dbRelatedCategories ]
    res__Dbcategories(related_categories, request, res)    
    return res.success()