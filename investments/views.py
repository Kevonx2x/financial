from django.shortcuts import render, redirect, get_object_or_404
from .models import Investment
from .forms import InvestmentForm

def investment_list(request):
    investments = Investment.objects.all()
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investment_list')  
    else:
        form = InvestmentForm()

    return render(request, 'investments/investments_list.html', {
        'investments': investments,
        'form': form,
    })

def edit_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            return redirect('investment_list')
    else:
        form = InvestmentForm(instance=investment)
    return render(request, 'investments/edit_investment.html', {'form': form})

def delete_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        investment.delete()
        return redirect('investment_list')
    return render(request, 'investments/delete_investment.html', {'investment': investment})

from django.shortcuts import render, redirect
from .forms import InvestmentForm

def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('investment_list')
    else:
        form = InvestmentForm()
    return render(request, 'investments/add_investment.html', {'form': form})

