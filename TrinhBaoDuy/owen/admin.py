from django.contrib import admin
from .models import Category



class CateAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']



admin.site.register(Category, CateAdmin)