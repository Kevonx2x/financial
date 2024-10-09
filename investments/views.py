from django.shortcuts import render
from .models import Investment

# Create your views here.
def investments_list(request):
    investments = Investment.objects.all()
    return render(request, 'investments/investments_list.html', {'investments': investments})
