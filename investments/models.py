from django.db import models

class Investment(models.Model):
    name = models.CharField(max_length=100)  
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.IntegerField(default=1)  
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  
    investment_type = models.CharField(
        max_length=50,
        choices=[('Stocks', 'Stocks'), ('Bonds', 'Bonds'), ('Real Estate', 'Real Estate'), ('Gold', 'Gold'), ('ETFs', 'ETFs')],
    )

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.investment_type})"
    
    def save(self, *args, **kwargs):

        if self.quantity and self.amount:
            self.total_cost = self.quantity * self.amount
        super().save(*args, **kwargs)
