from django.contrib import admin

# Register your models here.
from .models import Routers, RoutersType, RouterBackups


class RoutersAdmin(admin.ModelAdmin):
    list_display = ['id', 'devtype', 'addr', 'port', 'lastbackup', 'backup_result', 'identity', 'sleeptime', 'isActivated']
    search_fields = ['id', 'addr', 'identity']


class RoutersTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type']


class RouterBackupsAdmin(admin.ModelAdmin):
    list_display = ['id', 'dev_id', 'date', 'file_name', 'time_backup']
    search_fields = ['id', 'file_name', ]


admin.site.register(Routers, RoutersAdmin)
admin.site.register(RoutersType, RoutersTypeAdmin)
admin.site.register(RouterBackups, RouterBackupsAdmin)
