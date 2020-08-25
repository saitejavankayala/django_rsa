from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from rest_framework.decorators import api_view

from api.models import register
from api.serializer import RegisterSerializer, loginSerializer

'''
@api_view(['POST'])
def registration(request):
    if request.method == 'POST':
        reg_data = JSONParser().parse(request)
        reg_serializer = RegisterSerializer(data=reg_data)
        if reg_serializer.is_valid():
            reg_serializer.save()
            return JsonResponse({'message': 'successfully registrated!'}, status=status.HTTP_204_NO_CONTENT)

        return JsonResponse(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


@api_view(['POST', ])
def registration(request):
    if request.method == 'POST':
        username = list(request.data.values())[0]
        usr = register.objects.filter(username=username).exists()
        if usr:
            data = {}
            data['response'] = 'username already exists'
            return Response(data)

        else:
            serializer = RegisterSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                account = serializer.save()
                data['response'] = 'successfully registered new user.'
                data['email'] = account.email
                data['username'] = account.username
                data['phonenumber'] = account.phonenumber
                data['password'] = account.password

            else:
                data = serializer.errors
            return Response(data)


@api_view(['POST'])
def login(request):
    username = list(request.data.values())[0]
    password = list(request.data.values())[1]
    usr = register.objects.filter(username=username).exists()
    data = {}
    if usr and password:
        data['response'] = 'successfully login.'
    else:
        data['response'] = 'login credentianls is wrong'
    return Response(data)
