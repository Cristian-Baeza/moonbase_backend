from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Favorite(models.Model):
    uri = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    user = models.ForeignKey(User, related_name='favorites', on_delete=models.CASCADE)

    def __str__(self):
        return f"Id:{self.id}--{self.name}"