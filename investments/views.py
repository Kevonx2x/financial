from django.shortcuts import render, get_object_or_404, redirect
from .models import Investment
from .forms import InvestmentForm
from decimal import Decimal
from .utils import get_investment_type_name 


def investments_list(request):
    # Get all investments to display
    investments = Investment.objects.all()

    # Handle form submission (confirmation)
    if request.method == 'POST':
        investment_id = request.POST.get('investment_id')

        if investment_id:
            investment = Investment.objects.get(id=investment_id)
            # Here, confirm the investment purchase
            # You can add logic to update database or notify the user, etc.
            return render(request, 'investments/confirmation.html', {'investment': investment})
        else:
            return render(request, 'investments/investments_list.html', {'error': 'No investment selected.', 'investments': investments})

    return render(request, 'investments/investments_list.html', {'investments': investments})


def investment_confirm(request):
    if request.method == 'POST':
        # Get form data
        investment_type = request.POST.get('investment_type')
        investment_name_price = request.POST.get('investment_name', '').split('_')
        quantity = int(request.POST.get('quantity', 1))
        
        if len(investment_name_price) != 2:
            return redirect('investments:investments_list')
            
        investment_id, price = investment_name_price
        price_per_unit = Decimal(price)
        
        # Get the actual investment name using the ID
        investment_name = get_investment_name(investment_id)  # This line gets the proper name
        
        # Create investment object
        investment = Investment(
            investment_type=get_investment_type_name(investment_type),
            name=investment_name,  # Now this will be the actual name like "Apple" instead of just the ID
            quantity=quantity,
            amount=price_per_unit
        )
        
        investment.save()
        
        return render(request, 'investments/investment_confirm.html', {
            'investment': investment
        })


def get_investment_type_name(type_id):
    investment_types = {
        '1': 'Stocks',
        '2': 'Precious Metals',
        '3': 'Bonds',
        '4': 'Real Estate'
    }
    return investment_types.get(type_id, '')

def get_investment_name(investment_id):
    investment_names = {
        '1': 'Apple',
        '2': 'S&P 500',
        '3': 'Dow Jones',
        '4': 'Gold',
        '5': 'Silver',
        '6': 'Platinum',
        '7': 'US Treasury Bond',
        '8': 'Corporate Bond',
        '9': 'Municipal Bond',
        '10': 'Vanguard REIT (VNQ)',
        '11': 'Blackstone REIT (BREIT)',
        '12': 'Prologis Inc. (PLD)'
    }
    return investment_names.get(investment_id, '')

# Edit an existing investment
def edit_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            return redirect('investment_list')  # Or wherever you want to redirect after saving
    else:
        form = InvestmentForm(instance=investment)

    return render(request, 'investments/edit_investment.html', {'form': form})

# Delete an investment
def delete_investment(request, id):
    investment = get_object_or_404(Investment, id=id)
    
    if request.method == 'POST':
        investment.delete()
        return redirect('investments:investments_list')  # Redirect after deleting

    return render(request, 'investments/delete_investment.html', {'investment': investment})

# Finalize investment
def finalize_investment(request, id):
    investment = get_object_or_404(Investment, pk=id)

    if request.method == 'POST':
        investment.status = 'finalized'
        investment.save()

        return redirect('investments:investments_list')  # Or a success page like 'finalized_investment'
    
    return render(request, 'investments/finalize_investment.html', {'investment': investment})
