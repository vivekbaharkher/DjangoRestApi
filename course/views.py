from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Subject, Course
from .serializers import SubjectSerializers , SubjectDetailSerializers , CourseSerializers ,CourseDetailSerializers
from rest_framework.generics import ListAPIView #pigenation
from .pagiantion import LargeResultsSetPagination

#pagination
class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers
    pagination_class = LargeResultsSetPagination


# Create your views here.
# Create Course View
class CourseDetailView(APIView):
#     id=1
# course=Course.objects.get(id=id)
# students_in_course = course.subjects.all()
    def get(self,request,*args,**kwargs):
        id =kwargs.get('id')
        print(id)
        try:
            course=Course.objects.get(id=id)
            subject_in_course = course.subjects.all()
        except Course.DoesNotExist:
            return Response({"error":"Course not Found"},status=404)
        serializer=SubjectSerializers(subject_in_course,many=True)
        return Response(serializer.data)
    # def post(self,request):
    #     course_serializer = CourseDetailSerializers(data=request.data)
    #     course_serializer.is_valid(raise_exception=True)
    #     course_serializer.save()
    #     return Response(course_serializer.data,status=201)
    
    
    def post(self,request):
        Course_serializer = CourseDetailSerializers(data=request.data)
        Course_serializer.is_valid(raise_exception=True)
        Course_serializer.save()
        
            # validated_data = recipe_serializer.validated_data
            # recipe = Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer = RecipeCreateSerializer(recipe)
        return Response(Course_serializer.data,status=201)
# Create Subject View

class SubjectDetailView(APIView):
    def get(self,request):
        title = request.query_params.get('title')
        print(title)
        if title is not None:
            subject = Subject.objects.filter(name__icontains=title)
        else:
            subject = Subject.objects.all()
        serializer = SubjectSerializers(subject,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        subject_serializer = SubjectDetailSerializers(data=request.data)
        subject_serializer.is_valid(raise_exception=True)
        subject_serializer.save()
        
            # validated_data = recipe_serializer.validated_data
            # recipe = Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer = RecipeCreateSerializer(recipe)
        return Response(subject_serializer.data,status=201)