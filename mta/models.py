from django.db import models

# Create your models here.

class Team(models.Model):
    title = models.CharField(max_length=30)
    score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
