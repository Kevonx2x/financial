from django.urls import path
from . import views

app_name = 'investments'

urlpatterns = [
    path('investments/', views.investments_list, name='investments_list'),
    path('investments/confirm/', views.investment_confirm, name='investment_confirm'),
    path('finalize_investment/<int:id>/', views.finalize_investment, name='finalize_investment'),
    path('edit_investment/<int:id>/', views.edit_investment, name='edit_investment'),
    path('delete_investment/<int:id>/', views.delete_investment, name='delete_investment'),
]

