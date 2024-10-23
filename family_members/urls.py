from django.urls import path
from . import views

urlpatterns = [
    path('', views.family_member_list, name='family_member_list'), 
    path('new/', views.family_member_create, name='family_member_create'),  
    path('edit/<int:pk>/', views.family_member_edit, name='family_member_edit'),  
    path('delete/<int:pk>/', views.family_member_delete, name='family_member_delete'),
]

