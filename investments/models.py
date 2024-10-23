from django.db import models

class Investment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    investment_type = models.CharField(max_length=50, choices=[
        ('Stocks', 'Stocks'),
        ('Bonds', 'Bonds'),
        ('Real Estate', 'Real Estate'),
        ('Gold', 'Gold'),
        ('ETFs', 'ETFs'),
    ])

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.investment_type})"
