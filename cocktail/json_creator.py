# def create_json():
import csv
from collections import defaultdict


def select_cocktail(number):
    cocktail_list = []
    with open('./cocktail/data/cocktail_recipe.csv', 'r') as raw:
        drinks = csv.reader(raw)
        headers = next(drinks, None)
        print(headers)

        for record in drinks:
            cocktail_list.append(record)

        for i in range(0, len(cocktail_list)):
            print(cocktail_list[i])

        print(cocktail_list[0])
        # print(record)
    return cocktail_list[number], headers


def create_json(cocktail):
    print(select_cocktail(0))


class Cocktail:
    pass
# return json_data