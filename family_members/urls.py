# family_members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.family_members_list, name='family_members_list'),  
    path('<int:id>/', views.family_member_detail, name='family_member_detail'), 
]
