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

def keyboard(request):
    return JsonResponse({
        'type': 'buttons',
        'buttons': ['오늘', '안부', '비행기가격']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '오늘':
        today = "오늘 급식"

        return JsonResponse({
            'message': {
                'text': today
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })
    elif datacontent == '내일':
        tomorrow = "내일 급식"

        return JsonResponse({
            'message': {
                'text': tomorrow
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘', '내일']
            }

        })
