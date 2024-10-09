from django.db import models

# Create your models here.
class FamilyMember(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Investment(models.Model):
    name = models.CharField(max_length=50)
    investment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    family_member = models.ForeignKey(FamilyMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - ({self.investment_amount})"