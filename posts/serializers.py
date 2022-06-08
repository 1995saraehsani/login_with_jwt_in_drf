from django.db import models
from rest_framework import fields, serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=('id','author','title','body','date')