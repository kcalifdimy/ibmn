from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ibmn.users.models import User


ADDITIONAL_USER_FIELDS = (
    (None, {'fields': ('first_name','last_name','email', )}),)


class MyUserAdmin(UserAdmin):
    model = User

    add_fieldsets = UserAdmin.add_fieldsets + ADDITIONAL_USER_FIELDS
    list_display = ('first_name','last_name','email','gender')
    list_editable = ('gender',)


admin.site.register(User, MyUserAdmin)
