from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Your training view (for logged-in users)
    path('', views.training_view, name='training_view'), 

    # Login view (for unauthenticated users)
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
