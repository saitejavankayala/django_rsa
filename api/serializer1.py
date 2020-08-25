from rest_framework import serializers
from api.models import register


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = register
        fields = ('username',
                  'password',
                  'phonenumber',
                  'email'
                  )

    def save(self):
        account = register(
            email=self.validated_data['email'],
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
