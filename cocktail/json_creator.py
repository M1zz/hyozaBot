# def create_json():
import csv
from django.core.files import File
from collections import defaultdict

from django.http import JsonResponse


def select_cocktail(number):
    cocktail_list = []
    #./cocktail/data/cocktail_recipe.csv
    with open('/home/mizzking75/hyozaBot/cocktail/data/cocktail_recipe.csv', 'r') as raw:
        drinks = csv.reader(File(raw))
        headers = next(drinks, None)

        for record in drinks:
            cocktail_list.append(record)

    return cocktail_list[number]


def create_json(cocktail):

    data = JsonResponse({ 'version': '2.0', 'data': {'number':cocktail[0],'category':cocktail[1],'cockTailNameEn':cocktail[2],'cockTailNameKo':cocktail[3],'technique':cocktail[4],'glass':cocktail[5],'garnish':cocktail[6],'base':cocktail[7],'material1':cocktail[8],'material2':cocktail[9],'material3':cocktail[10],'material4:':cocktail[11]}})
    return data

class Cocktail:
    pass
# return json_data