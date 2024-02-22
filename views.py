from django.shortcuts import render
from kernel.http import Response
from profiles.decorators import load_profile

@load_profile
def get_all(request):
    """
    Get all categories, to the user select one
    """
    res = Response()
    return res.success()

@load_profile
def set_selected_category(request):
    res = Response()
    return res.success()
