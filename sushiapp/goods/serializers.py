from rest_framework import serializers
# from rest_framework.serializers import ModelSerializer

from .models import Category, Good


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class GoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = '__all__'