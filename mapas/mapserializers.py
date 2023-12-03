from rest_framework import serializers
from .models import City, Project, Product, ImageType, Image, Coordinate, Dictionary
from django.contrib.auth.models import User

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('idCity', 'name', 'state', 'country')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('idProject', 'name', 'city', 'users')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('idProduct', 'name', 'derived', 'idProject', 'idImage')

class ImageTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageType
        fields = ('idImageType', 'name', 'visible')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('idImage', 'name', 'image', 'idImageType')

class CoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinate
        fields = ('idCoordinate', 'geometry', 'properties', 'type', 'idImage')

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('idDictionary', 'label', 'class_name')