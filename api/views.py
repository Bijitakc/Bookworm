from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import permissions,generics,routers,status,viewsets
from .serializers import BookSerializer,RegisterUserSerializer,LoginSerializer
from rest_framework_simplejwt.tokens import AccessToken,RefreshToken
from .models import Book
import jwt,datetime

User=get_user_model()

class CustomUserCreate(APIView):
    permission_classes=[permissions.AllowAny]

    def post(Self,request):
        reg_serializer=RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser=reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#can be overrided
class Bookall(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    serializer_class=BookSerializer

    #added a search using slugname(better for SEO) ie searching via title in url
    #how this works is it gets the pk(now title) from the url then gets the matching object
    def get_object(self,queryset=None,**kwargs):
        item=self.kwargs.get('pk')
        return get_object_or_404(Book,title=item)

    def get_queryset(self):
        queryset=Book.objects.all()
        return queryset

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


# class Bookall(viewsets.ViewSet):
#     permission_classes=[permissions.AllowAny]
#     queryset=Book.objects.all()

#     def list(self,request):
#         serializer_class=BookSerializer(self.queryset,many=True)
#         return Response(serializer_class.data)

#     def retrieve(self,request,pk=None):
#         book=get_object_or_404(self.queryset,pk=pk)
#         serializer_class=BookSerializer(book)
#         return Response(serializer_class.data)

#gets a list of books(example of generics)
# class BookList(generics.ListAPIView):
#     queryset=Book.objects.all()
#     permission_classes=[permissions.AllowAny]
#     serializer_class=BookSerializer