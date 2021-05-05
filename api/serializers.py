from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from .models import Book

User=get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        exclude=('id',)

class RegisterUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(min_length=2,write_only=True)
    
    class Meta:
        model=User
        fields=('email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class LoginSerializer(serializers.Serializer):
    email=serializers.CharField(max_length=100,required=True)
    password=serializers.CharField(max_length=200,required=True)
    user = serializers.ReadOnlyField

    # custom validation
    def validate(self,attrs):
        attrs=super().validate(attrs)
        username=attrs['email']
        password=attrs['password']
        print(username,password)
        user=authenticate(username=username,password=password)
        print(user)
        if not user:
            raise seriializers.ValidationError(
                {"message":"Invalid Credentials"}
            )
        else:
            self.validated_user=user
            return attrs



