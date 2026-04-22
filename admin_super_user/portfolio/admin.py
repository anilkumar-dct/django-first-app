from django.contrib import admin

# Register your models here.
from .models import Portfolio, Project

admin.site.register(Portfolio)
admin.site.register(Project)