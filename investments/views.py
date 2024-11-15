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

def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        

        selected_investment_id = request.POST.get('investment')
        amount = request.POST.get('amount')
        date_invested = request.POST.get('date_invested')


        request.session['selected_investment_id'] = selected_investment_id
        request.session['investment_amount'] = amount
        request.session['investment_date'] = date_invested


        return redirect('investment_confirm')

    else:
        form = InvestmentForm()
    
    investments = Investment.objects.all()
    return render(request, 'investments/add_investment.html', {'form': form, 'investment_options': investments})


def investment_confirm(request):
    selected_investment_id = request.session.get('selected_investment_id')
    amount = request.session.get('investment_amount')
    date_invested = request.session.get('investment_date')

    if selected_investment_id:
        selected_investment = Investment.objects.get(id=selected_investment_id)
    else:
        selected_investment = None


    if not selected_investment:
        return redirect('add_investment')  

    return render(request, 'investments/investment_confirm.html', {
        'selected_investment': selected_investment,
        'amount': amount,
        'date_invested': date_invested
    })

def add_investment(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)

        selected_investment_id = request.POST.get('investment')
        amount = request.POST.get('amount')
        date_invested = request.POST.get('date_invested')

        request.session['selected_investment_id'] = selected_investment_id
        request.session['investment_amount'] = amount
        request.session['investment_date'] = date_invested

        return redirect('investment_confirm')

    else:
        form = InvestmentForm()

    investments = Investment.objects.all()
    return render(request, 'investments/add_investment.html', {'form': form, 'investment_options': investments})

