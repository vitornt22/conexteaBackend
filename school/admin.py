from django.contrib import admin
from .models import School, SchoolClass

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'director_name', 'inep_number')

@admin.register(SchoolClass)
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'school')
