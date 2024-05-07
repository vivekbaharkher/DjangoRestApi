from rest_framework import serializers
from .models import Course,Subject

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields= '__all__'
class CourseDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields =[
            'name',
            'description',
            'price',
        ]        
class SubjectSerializers(serializers.ModelSerializer):
    course=CourseSerializers()
    class Meta:
        model = Subject
        fields= '__all__'
class SubjectDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields =[
            'course',
            'name',
            'description',
            'photo',
        ]