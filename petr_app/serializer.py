from rest_framework import serializers
from .models import Category, Tag, Post


class CategorySerialiser(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']