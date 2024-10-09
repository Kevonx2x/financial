from django.contrib import admin
from .models import FamilyMember, Investment

# Register your models here.
admin.site.register(FamilyMember)
admin.site.register(Investment)

