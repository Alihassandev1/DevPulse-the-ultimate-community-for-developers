from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'uid', 'created_at', 'updated_at']
    readonly_fields = ['uid', 'created_at', 'updated_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'uid']
