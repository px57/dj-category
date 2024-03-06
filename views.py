from django.shortcuts import render
from django.db.models import Q

from kernel.http import Response
from kernel.http import load_response
from kernel.i18n.models import translateDBQuerySet
from kernel.http.decorators import load_json

from profiles.decorators import load_profile

from category.__rules__.stack import CATEGORY_RULESTACK
from category.models import Category
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
    
    dbSelectedCategories = form.cleaned_data['selected_list_id']
    _in.set_selected_categories(dbSelectedCategories)
    res__Dbcategories(dbSelectedCategories, request, res)
    return res.success()