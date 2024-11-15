from django.urls import path
from . import views

urlpatterns = [
    path('', views.family_member_list, name='family_member_list'),
    path('add/', views.add_family_member, name='add_family_member'),
    path('edit/<int:pk>/', views.family_member_edit, name='family_member_edit'),
    path('delete/<int:pk>/', views.family_member_delete, name='family_member_delete'),
    path('confirm_delete/<int:pk>/', views.family_member_delete, name='family_member_confirm_delete'),

]
