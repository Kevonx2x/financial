from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('family_members.urls')),  
    path('', include('investments.urls')),  
]
