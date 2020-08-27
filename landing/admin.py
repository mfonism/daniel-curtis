from django.contrib import admin

from .models import WantToSee


class WantToSeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(WantToSee, WantToSeeAdmin)
