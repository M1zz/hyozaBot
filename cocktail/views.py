from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from cocktail import json_creator as JC
import json


def index(request):
    return JsonResponse({
        'type': 'welcome',
        'message': 'HelloDjango'
    })


@csrf_exempt
def recipe(request, drinknumber):
    cocktail = JC.select_cocktail(drinknumber)
    print(cocktail,type(cocktail))
    jason_data = JC.create_json(cocktail)

    return jason_data
