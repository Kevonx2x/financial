from django.shortcuts import render
from .models import Investment

def investments_list(request):
    investments = Investment.objects.all()
    return render(request, 'investments/investments_list.html', {'investments': investments})

def investment_detail(request, id):
    investment = Investment.objects.get(id=id)
    return render(request, 'investments/investment_detail.html', {'investment': investment}) 
