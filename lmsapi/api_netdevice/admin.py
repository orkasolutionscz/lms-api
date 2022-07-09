from django.contrib import admin

# Register your models here.
from .models import Netcontypes, Wlanmodes


class NetconTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'typ']


class WlanModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'apmode']


admin.site.register(Netcontypes, NetconTypeAdmin)
admin.site.register(Wlanmodes, WlanModeAdmin)
