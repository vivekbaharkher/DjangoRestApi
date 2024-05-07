from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.response import Response
from .models import Recipe
from .serializers import RecipeSerializer,RecipeCreateSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class RecipeViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Recipe.objects.all()
    queryset = Recipe.objects.select_related('title','user').prefetch_related("ingredient")
    serializer_class = RecipeSerializer

class RecipeListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        title = request.query_params.get('title')
        print(title)
        if title is not None:
            recipes = Recipe.objects.filter(title__icontains=title,user=request.user)
        else:
            recipes = Recipe.objects.filter(user=request.user)
        serializer = RecipeSerializer(recipes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        recipe_serializer = RecipeCreateSerializer(data=request.data)
        recipe_serializer.is_valid(raise_exception=True)
        recipe_serializer.save(user=request.user)
            # validated_data = recipe_serializer.validated_data
            # recipe = Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer = RecipeCreateSerializer(recipe)
        return Response(recipe_serializer.data,status=201)

class RecipeDetailView(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        print(id)
        try:
            recipe = Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return Response({
                'msg':'Recipe not found'
            },status=404)

        serializer = RecipeSerializer(recipe)
        # return Response(serializer.data)
        return Response(serializer.data)
    def put(self,request,*args,**kwargs):
        id=kwargs.get('id')
        recipe=Recipe.objects.get(id=id)
        recipe_serializer=RecipeCreateSerializer(recipe,data=request.data)
        if recipe_serializer.is_valid():
            recipe_serializer.save(updated_by_user=request.user)
            return Response(recipe_serializer.data)
        else:
            print(recipe_serializer.errors)
            return Response(recipe_serializer.errors)


@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])

def hello(request):
    return Response({
        'data':"Hello World"
    })



@api_view()
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])

def who(request):
    user = request.user
    return Response({
        'user':user.username,
        'data':"Hello World"
    })





@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
def list_recipe(request):
    if request.method == "POST":
        print(request.data)
        recipe_serializer = RecipeCreateSerializer(data=request.data)
        if recipe_serializer.is_valid(raise_exception=True):
            recipe_serializer.save(user=request.user)
            # validated_data = recipe_serializer.validated_data
            # recipe = Recipe(user=request.user,**validated_data)
            # recipe.save()
            # recipe_serializer = RecipeCreateSerializer(recipe)
            return Response(recipe_serializer.data,status=201)
        else:
            print(recipe_serializer.errors)
            return Response(recipe_serializer.errors)
    else:
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes,many=True)
        response_data = serializer.data
        return Response(response_data)


@api_view(['GET','DELETE','PUT'])
def recipe_detail(request,id):

    try:
        recipe = Recipe.objects.get(id=id)
    except Recipe.DoesNotExist:
        return Response(data={"detail":"Requested recipe doesn't exist"},status=404)
    
    if request.method == "GET":
        # recipe = Recipe.objects.get(id=id)
        recipe_serializer = RecipeSerializer(recipe)
        return Response(recipe_serializer.data)
    
    elif request.method =="PUT":
        # recipe = Recipe.objects.get(id=id)
        recipe_serializer = RecipeSerializer(recipe,data=request.data)
        if recipe_serializer.is_valid():
            recipe_serializer.save()
            return Response(recipe_serializer.data)
        else:
            return Response(recipe_serializer.errors)

    elif request.method == "DELETE" :
        # recipe = Recipe.objects.get(id=id)
        recipe.delete()
        return Response(status=204)

@api_view()
def list_manual(request):
    recipes = Recipe.objects.all()

    data = [

    ]
    
    for recipe in recipes:

        recipe_object = {
            'id':recipe.id,
            'title_manual':recipe.title,
            'description':recipe.description,
            'time_required':recipe.time_required

        }
        print(recipe_object)
        data.append(
            recipe_object
        )
    print(data)
    response_data = {
        'recipes':data
    }
    return Response(response_data)


# Create your views here.
