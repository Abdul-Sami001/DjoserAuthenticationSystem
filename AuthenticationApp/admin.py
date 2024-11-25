from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('email',)  # Use a tuple for search_fields
    ordering = ('email', 'id')
    filter_horizontal = ()
    #These fields will override the UserModelAdmin
    #list_display = ('id', 'email', 'name', 'is_active', 'is_admin')
    # list_filter = ('is_admin')
    # fieldsets = (
    #     ('UserCredentials',{'fields:'('email', 'password')}),
    #     ('Personal info', {'fields':('name')}),
    #     ('Permissions',{'fields':('is_admin', 'is_active')}),
    # )
    #search_fields = ('email')
    #ordering = ('email', 'id')
    #filter_horizontal = ()
    
admin.site.register(User, UserModelAdmin)