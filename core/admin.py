from django.contrib import admin
from core import models


class Command(admin.ModelAdmin):
    list_display = ('name', 'dm')
admin.site.register(models.Command, Command)
