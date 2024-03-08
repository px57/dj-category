"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views

urlpatterns = [
    path(
        'get_all/', 
        views.get_all, 
        name='category__get_all'
    ),
    path(
        'set_selected_category/', 
        views.set_selected_category, 
        name='category__set_selected_category'
    ),
    path(
        'get_related_categories/', 
        views.get_related_categories, 
        name='category__get_related_categories'
    ),
]