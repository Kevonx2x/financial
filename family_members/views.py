from django.shortcuts import render
from .models import FamilyMember

# Create your views here.
def family_members(request):
    members = FamilyMember.objects.all() 
    return render(request, 'family_members/family_members_list.html', {'members': members})
