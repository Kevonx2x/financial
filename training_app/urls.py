from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('', views.training_view, name='training_view'), 


    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
