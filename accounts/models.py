from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=258)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=258)

    def __str__(self):
        return self.name
    
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser):

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser',
    )
