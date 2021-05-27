from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import permissions,generics,routers,status,viewsets
from .serializers import BookSerializer
from .models import Book
import jwt,datetime


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





# class updateprofile()
