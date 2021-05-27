from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import permissions,generics,routers,status,viewsets
from .serializers import RegisterUserSerializer,LoginSerializer,UserChangePasswordSerializer
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
User=get_user_model()

class CustomUserCreate(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterUserSerializer
    permission_classes=[permissions.AllowAny]

class LoginView(APIView):
    serializer_class=LoginSerializer

    def post(self,request):
        loginRSerializer=LoginSerializer(data=request.data)
        #checks the validation in serialiizer
        if loginRSerializer.is_valid():
            accesstoken=AccessToken.for_user(loginRSerializer.validated_user)
            print("this")
            print(loginRSerializer.validated_user)
            return Response({"access_token":str(accesstoken)})
        else:
            return Response(loginRSerializer.errors,status=status.HTTP_400_BAD_REQUEST)


class UserChangePassword(APIView):
    serializers_class=UserChangePasswordSerializer
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        userPasswordSerializer=UserChangePasswordSerializer(
            data=request.data
        )

        if userPasswordSerializer.is_valid():
            user=request.user
            user.set_password(
                userPasswordSerializer.validated_data['new_password']
            )
            user.save()
            return Response({"message":"Successful"})
        else:
            return Response(userPasswordSerializer.errors,status=status.HTTP_400_BAD_REQUEST)

# user presses logout and the access tokens get blaclisted 
class  BlacklistTokenView(APIView):
    permission_classes=[permissions.AllowAny]

    def post(self,request):
        try:
            refresh_token=request.data["refresh_token"]
            token=RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)