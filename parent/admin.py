from django.contrib import admin

from parent.models import Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')

