from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import BaseUser, Student, Trainer


@admin.register(BaseUser)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('role',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (None, {'fields': ('role',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions'
            ),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('role',),
        }),
    )


admin.site.register((Student, Trainer))
