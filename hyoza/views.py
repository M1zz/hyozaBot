from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


def index(request):
    return JsonResponse({
        'type': 'welcome',
        'message': 'HelloDjango'
    })


@csrf_exempt
def sayhello(request):
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'simpleText': {
                        'text': "hello I'm Ryan"
                    }
                }
            ]
        }
    })


@csrf_exempt
def showhello(request):
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [
                {
                    'simpleImage': {
                        'imageUrl': "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        'altText': "hello I'm Ryan"
                    }
                }
            ]
        }
    })


@csrf_exempt
def showprofile(request):
    return JsonResponse({
        "version": "2.0",
        "data": {
            "first": {
                "msg": "안녕하세요 반가워요 이현호입니다",
                "name": "HyunhoLee",
                "position": "Junior Programmer"}
        }
    })


@csrf_exempt
def showticketprice(request):

    depart_company = "피치항공"
    depart_price = "258,984"
    depart_takeoff = "15: 35"
    depart_landing = "17: 25"

    return_company = "피치항공"
    return_price = "258,984"
    return_takeoff = "07: 40"
    return_landing = "9: 30"

    return JsonResponse({
        "version": "2.0",
        "data": {
            "depart_ticket_1": {
                "depart_company": depart_company,
                "depart_price": depart_price,
                "depart_takeoff": depart_takeoff,
                "depart_landing": depart_landing
            },
            "return_ticket_1": {
                "return_company": return_company,
                "return_price": return_price,
                "return_takeoff": return_takeoff,
                "return_landing": return_landing
            }

        }
    })
