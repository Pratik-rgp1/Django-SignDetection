from django.contrib import admin

from .models import *

# admin.site.register(Profile)

@admin.action(description='Mark selected profiles as verified')
def make_verified(modeladmin, request, queryset):
    queryset.update(is_verified=True)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'is_verified']
    actions = [make_verified]

admin.site.register(Profile, ProfileAdmin)

