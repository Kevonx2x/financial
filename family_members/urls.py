from django.urls import path
from . import views

urlpatterns = [
    path('', views.family_member_list, name='family_member_list'),  # List view at /family_members/
    path('new/', views.family_member_create, name='family_member_create'),  # Create new family member
    path('edit/<int:pk>/', views.family_member_edit, name='family_member_edit'),  # Edit a family member
    path('delete/<int:pk>/', views.family_member_delete, name='family_member_delete'),  # Delete a family member
]

