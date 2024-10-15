from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self
        