from django.shortcuts import render, redirect, get_object_or_404
from .models import FamilyMember
from .forms import FamilyMemberForm


def family_member_list(request):
    family_members = FamilyMember.objects.all()
    return render(request, 'family_member_list.html', {'family_members': family_members})

def family_member_create(request):
    if request.method == "POST":
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('family_member_list')
    else:
        form = FamilyMemberForm()
    return render(request, 'family_member_form.html', {'form': form})


def family_member_edit(request, pk):
    family_member = get_object_or_404(FamilyMember, pk=pk)
    if request.method == "POST":
        form = FamilyMemberForm(request.POST, instance=family_member)
        if form.is_valid():
            form.save()
            return redirect('family_member_list')
    else:
        form = FamilyMemberForm(instance=family_member)
    return render(request, 'family_member_form.html', {'form': form})

def family_member_delete(request, pk):
    family_member = get_object_or_404(FamilyMember, pk=pk)
    if request.method == "POST":
        family_member.delete()
        return redirect('family_member_list')
    return render(request, 'family_member_confirm_delete.html', {'family_member': family_member})

def home(request):
    return render(request, 'pages/home.html')
