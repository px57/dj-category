from django.shortcuts import render
from kernel.http import Response

def __empty__(request):
    res = Response()
    return res.success()
