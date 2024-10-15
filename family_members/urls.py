# family_members/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This maps the root URL to the home view
    path('list/', views.family_members_list, name='family_members_list'),  # URL for the list of members
    path('<int:id>/', views.family_member_detail, name='family_member_detail'),  # URL for me
]
