from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

'''
    - Create an **(GET)** api endoint that returns the following  json response:
        
        { "**slackUsername**": String, "**backend**": Boolean, "**age**": Integer, "**bio**": String }
        
        - SlackUsername should be a **string** datatype and your slack username
        - Backend should be a **boolean** datatype
        - Age should be an  **integer** datatype
        - Bio(description about yourself) should be a **string** datatype
'''

def json_res_view(request):
    data = {}
    data['slackUsername'] = 'henzyd'
    data['backend'] = True
    data['age'] = 18
    data['bio'] = 'Hi my name is Uchechukwu Anachuna I\'m a Fullstack Web Developer proficient in JavaScript, ReactJS, Python and Django'
    return JsonResponse(data)