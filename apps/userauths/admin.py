from django.contrib import admin

from apps.userauths.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'bio',)
    list_display_links = ('email', 'username',)