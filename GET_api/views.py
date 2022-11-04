from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import EnumSerializer
from rest_framework.response import Response
from rest_framework import status
import numpy as np
# import requests
# import json
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
        operation_type = serializer.validated_data['operation_type']
        operation = str(operation_type.strip().lower())

        try:
            x = int(serializer.validated_data['x'])
            y = int(serializer.validated_data['y'])
        except:
            return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        result = 0
        if operation == 'addition':
            result += x + y
        elif operation == 'subtraction':
            result += x - y
        elif operation == 'multiplication':
            result += x * y
        elif operation:
            list_operation = operation.split()
            x = 0
            y = 0
            opera = ''
            new_l = []

            for i, item in enumerate(list_operation):
                if item.isdigit():
                    new_l.append(int(list_operation[i]))
                else:
                    try:
                        uche = int(item)
                    except:
                        uche = None
                    if uche is not None:
                        new_l.append(int(list_operation[i]))
                    else:
                        continue
                    ### NOTE make it possible to add multiple number

            if len(new_l) == 2 :
                def test(*args):
                    if 'add' in list_operation:
                        return sum(tuple(args))
                    elif 'subtract' in list_operation:
                        return np.subtract(*args)
                    elif 'multiply' in list_operation:
                        return np.multiply(*args)

                result += test(*new_l)
            else:
                return Response(status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        data = {}
        data['slackUsername'] = 'henzyd'
        data['result'] = result
        data['operation_type'] = operation
        # print(data)
        return Response(data=data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['POST'])
# def json_enum_view(request):
#     '''
#         { “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }
#     '''
#     if request.method == 'POST':
#         # url = "https://get-api23.herokuapp.com/enum/"
#         # data = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
#         serializer = EnumSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         # data = {serializer.data}
#         # headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#         # r = requests.post(url, data=json.dumps(data), headers=headers)
#         operation = str(serializer.validated_data['operation_type'].strip().lower())
#         x = int(serializer.validated_data['x'])
#         y = int(serializer.validated_data['y'])
#         result = 0
#         if operation == 'addition':
#             result += x + y
#         elif operation == 'subtraction':
#             result += x - y
#         elif operation == 'multiplication':
#             result += x * y
#         data = {}
#         data['slackUsername'] = 'henzyd'
#         data['result'] = result
#         data['operation_type'] = operation
#         return JsonResponse(data=data)

#     return Response(status=status.HTTP_400_BAD_REQUEST)