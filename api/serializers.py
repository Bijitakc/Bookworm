from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Book

User=get_user_model()

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        exclude=('id',)

class RegisterUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    username=serializers.CharField(required=True)
    password=serializers.CharField(min_length=2,write_only=True)
    
    class Meta:
        model=User
        fields=('username','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=('username','email','password')
#         extra_kwargs={'password':{'write_only':True}}

#     def create(self,validated_data):
#         password=validated_data.pop('password',None)
#         instance=self.Meta.model(**validated_data)
#         if password is not None:
#             instance.set_password(password)
#         instance.save()
#         return instance




