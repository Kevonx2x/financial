from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm  # Or your custom form if you have one
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use the built-in user creation form or your custom one
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})
