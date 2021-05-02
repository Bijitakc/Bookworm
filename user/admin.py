from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model=CustomUser

    fieldsets=(
        *UserAdmin.fieldsets,
        (
            'Mainform',
            {
                'fields':(
                    'number',
                    'address',
                    'bio'
                )
            }
        )
    )
admin.site.register(CustomUser,CustomUserAdmin)