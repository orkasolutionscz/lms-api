from django.db import models

from django.core.exceptions import ValidationError

# Create your models here.


class Routers(models.Model):
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True, blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    sleeptime = models.SmallIntegerField()

    class Meta:
        db_table = 'routers'

    def __str__(self):
        return '{}:{}'.format(self.addr, self.port)


class RoutersOld(models.Model):
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True, blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    sleeptime = models.SmallIntegerField()

    class Meta:

        managed = False
        db_table = 'routers'


class MigrateRouters:
    def __init__(self):
        self.from_db = 'rbackup'

    def migrate_data(self):
        rows = RoutersOld.objects.using('rbackup').all()
        try:
            for row in rows:
                newrouter = Routers(id=row.id, addr=row.addr, identity=row.identity, sleeptime=row.sleeptime, port=row.port)
                # newrouter.user_id = 1
                newrouter.save(using='default')
            return True
        except:
            raise


