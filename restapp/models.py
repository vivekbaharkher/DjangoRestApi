from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Ingredient(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    ingredient=models.ManyToManyField(Ingredient)
    title=models.CharField(max_length=30)
    description=models.TextField()
    time_required=models.CharField(max_length=23)
    updated_by_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="updated_by")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.title
    