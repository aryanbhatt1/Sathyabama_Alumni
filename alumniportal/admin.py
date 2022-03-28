from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass