from django.db import models


class RoutersType(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'routerstype'
        ordering = ['type']

    def __str__(self):
        return self.type


class Routers(models.Model):
    BACKUP_STATUS = (
        ('N', 'Neprobehlo'),
        ('OK', 'Uspesne'),
        ('ERLOG', 'Neuspesne prihlaseni'),
        ('ERDOWN', 'Chyba pri prenosu zalohy')
    )
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    firmware = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True, blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    backup_result = models.CharField( max_length=10, default='N', choices=BACKUP_STATUS)
    sleeptime = models.SmallIntegerField(default=0)
    isActivated = models.BooleanField(default=False)
    dev_info = models.TextField(blank=True)
    devtype = models.ForeignKey(RoutersType, related_name='router_type', on_delete=models.CASCADE, default='1')

    class Meta:
        db_table = 'routers'

    def __str__(self):
        return f'{self.addr} / {self.port}'


class RouterBackups(models.Model):
    dev_id = models.ForeignKey(Routers, related_name='router_backups', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=500)
    type = models.CharField(max_length=15)
    file_ext = models.CharField(max_length=15, blank=True, null=True)
    time_backup = models.DecimalField(default=0, max_digits=6, decimal_places=1)

    class Meta:
        db_table = 'routers_backups'

    def __str__(self):
        return f'{self.date} - {self.file_name}'
