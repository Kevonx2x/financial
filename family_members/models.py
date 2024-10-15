# family_members/models.py

from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name  
