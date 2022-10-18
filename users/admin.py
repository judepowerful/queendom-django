from django.contrib import admin

from  users.models import Account, Profile


admin.site.register(Account)
admin.site.register(Profile)