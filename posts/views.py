from typing import Generic

from rest_framework import serializers
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer
     
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    queryset=Post.objects.all()
    serializer_class=PostSerializer