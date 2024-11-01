from django.urls import path
from . import views

urlpatterns = [
    path('investments/', views.investment_list, name='investment_list'),
    path('investments/edit/<int:id>/', views.edit_investment, name='edit_investment'),
    path('investments/delete/<int:id>/', views.delete_investment, name='delete_investment'),
    path('investments/add/', views.add_investment, name='add_investment'), 
]

