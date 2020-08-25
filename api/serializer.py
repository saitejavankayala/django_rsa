from rest_framework import serializers
from api.models import register
from .enc import *


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ('username',
                  'password',
                  'phonenumber',
                  'email'
                  )

    def save(self):
        email = encrypt(self.validated_data['email'].encode()),
        print(email)
        account = register(

            username=self.validated_data['username'],
            phonenumber=self.validated_data['phonenumber'],
            password=self.validated_data['password'],
        )
        account.save()
        return account


class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = (
            'username',
            'password',
        )
