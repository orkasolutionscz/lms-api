from django.contrib import admin

# Register your models here.
from .models import Routers, RoutersType


class RoutersAdmin(admin.ModelAdmin):
    list_display = ['id', 'addr', 'port', 'identity', 'sleeptime']
    search_fields = ['id', 'addr', ]


class RoutersTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']


admin.site.register(Routers, RoutersAdmin)
admin.site.register(RoutersType, RoutersTypeAdmin)
