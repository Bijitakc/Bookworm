from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from .utils import validate_password
# from rest_framework.exceptions import AuthenticationFailed
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
        fields=('email','first_name','last_name','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validated_data):
        password=validated_data.pop('password')
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            instance.is_active=True
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
            raise serializers.ValidationError(
                {"message":"Invalid Credentials"}
            )
        else:
            self.validated_user=user
            return attrs

class UserChangePasswordSerializer(serializers.Serializer):
    # email=serializers.CharField(max_length=100,required=True)
    password=serializers.CharField(required=True)
    confirm_password=serializers.CharField(required=True)
    new_password=serializers.CharField(required=True)

    def validate_new_password(self,value):
        print(value)
        validate_password_errors=validate_password(value)
        if not validate_password_errors:
            return value
        else:
            raise serializers.ValidationError(validate_password_errors)

    def validate(self, attrs):
        print("attrs")
        print(attrs)
        attrs=super().validate(attrs)
        if attrs['confirm_password'] != attrs['new_password']:
            raise serializers.ValidationError(
                {"message":"Password don't match"})
        # email=attrs.get('email')
        # print(email)
        request= self.context.get("request")
        user=authenticate(password=attrs.get('password'),username=request.user.username)
        if not user:
            raise serializers.ValidationError({"message":"Invalid Password."})
        else:
            return attrs
            

