from django.contrib import admin

# Register your models here.
from .models import Netcontypes, Wlanmodes, Wlanfreqs, Wlanfranges


class NetconTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'typ']


class WlanModeAdmin(admin.ModelAdmin):
    list_display = ['id', 'apmode']


class WlanfrangesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class WlanfreqsAdmin(admin.ModelAdmin):
    list_display = ['id', 'ref_ad', 'name', 'freq']


admin.site.register(Netcontypes, NetconTypeAdmin)
admin.site.register(Wlanmodes, WlanModeAdmin)
admin.site.register(Wlanfranges, WlanfrangesAdmin)
admin.site.register(Wlanfreqs, WlanfreqsAdmin)
