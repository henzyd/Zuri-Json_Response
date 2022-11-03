from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import EnumSerializer
from rest_framework.response import Response
from rest_framework import status
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



@api_view(['POST'])
def json_enum_view(request):
    '''
        { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
    '''

    if request.method == 'POST':
        serializer = EnumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        operation = str(serializer.validated_data['operation_type'].strip().lower())
        x = int(serializer.validated_data['x'])
        y = int(serializer.validated_data['y'])
        result = 0
        if operation == 'addition':
            result += x + y
        elif operation == 'subtraction':
            result += x - y
        elif operation == 'multiplication':
            result += x * y
        # else:
        #     raise ValueError('this is not what was requested')
        print(serializer.validated_data['operation_type'])
        data = {}
        data['slackUsername'] = 'henzyd'
        data['result'] = result
        data['operation_type'] = operation
        print(data)
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)