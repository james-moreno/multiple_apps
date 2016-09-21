from django.db import models
from ..landr.models import Register
# Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=45)
    users = models.ManyToManyField(Register)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
