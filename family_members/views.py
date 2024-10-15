# family_members/views.py

from django.shortcuts import render
from .models import FamilyMember

# Create your views here.
def family_members_list(request):
    members = FamilyMember.objects.all() 
    return render(request, 'family_members/family_members_list.html', {'members': members})

def family_member_detail(request, id):
    member = FamilyMember.objects.get(id=id)
    return render(request, 'family_members/family_member_detail.html', {'member': member})

def home(request):
    return render(request, 'home.html')  # This will extend base.html
