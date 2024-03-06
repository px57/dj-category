
from django import forms
from django.db.models import Q

from kernel.interfaces.forms import InterfaceValidator  

from category.models import Category

import json

class SetSelectedCategoryForm(forms.Form):
    """
    Validate the request to set the selected category
    """

    _in = InterfaceValidator(required=True)

    selected_list_id = forms.CharField(
        required=True,
    )

    def clean_selected_list_id(self):
        """
        Selected list id
        """
        _in = self.cleaned_data['_in']
        try: 
            selected_list_id = json.loads(self.cleaned_data['selected_list_id'])
        except:
            raise forms.ValidationError(
                "selected_list_id is not a valid json"
            )

        # delete duplicates
        selected_list_id = list(set(selected_list_id))

        # check if the list is too long
        if _in.max_categories_per_user != '*':
            if _in.max_categories_per_user < len(selected_list_id):
                raise forms.ValidationError(
                    "selected_list_id is too long " + str(len(selected_list_id))
                )

        # check if the list is too short
        if _in.min_categories_per_user != '*':
            if _in.min_categories_per_user > len(selected_list_id):
                raise forms.ValidationError(
                    "selected_list_id is too short " + str(len(selected_list_id))
                )

        # check if the list is empty
        Query = Q()
        for id in selected_list_id:
            Query = Query | Q(id=id)

        if not Query:
            return Category.objects.none()
        
        # check if the list is valid
        dbCategories = Category.objects.filter(Query)
        if dbCategories.count() != len(selected_list_id):
            # show the list of id not found
            not_found = []
            for id in selected_list_id:
                if not dbCategories.filter(id=id).exists():
                    not_found.append(id)
            raise forms.ValidationError(
                f"selected_list_id {not_found} not found"
            )
        
        return dbCategories