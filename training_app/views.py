from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProgress

@login_required 
def training_view(request):

    user_progress = {
        up.video_id: up.completed for up in UserProgress.objects.filter(user=request.user)
    }

    context = {
        'user_progress': user_progress,
    }

    return render(request, 'pages/training.html', context)

