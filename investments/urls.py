from django.urls import path
from . import views

urlpatterns = [
    path('', views.investments_list, name='investment_list'),  # Update here if the function is named investments_list
    path('<int:id>/', views.investment_detail, name='investment_detail'),
]
