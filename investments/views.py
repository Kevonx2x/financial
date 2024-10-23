from django.shortcuts import render, redirect
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
