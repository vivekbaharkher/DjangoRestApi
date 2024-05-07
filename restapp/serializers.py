from rest_framework import serializers
from .models import Recipe 
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "email",
        ]


class RecipeSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model = Recipe
        fields = '__all__'


class RecipeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title',
                'description',
                'time_required',
                'updated_by_user',
                'user'
                ]
