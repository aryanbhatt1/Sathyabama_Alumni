from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Overview)
class OverviewAdmin(admin.ModelAdmin):
    pass


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    pass


admin.site.register(FacultyUser)
admin.site.register(Gender)
admin.site.register(Degree)
admin.site.register(YearOfCompletion)
admin.site.register(EmploymentType)
admin.site.register(PresentStatus)