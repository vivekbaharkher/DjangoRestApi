from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.name

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)
    description = models.TextField()
    photo=models.ImageField(upload_to="SubjectPhoto",null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    