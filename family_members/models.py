# family_members/models.py

from django.db import models

class FamilyMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.name  
