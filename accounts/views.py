from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
