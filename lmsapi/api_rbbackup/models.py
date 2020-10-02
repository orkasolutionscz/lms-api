from django.db import models


class RoutersType(models.Model):
    type = models.CharField(max_length=255)

    class Meta:
        db_table = 'routerstype'

    def __str__(self):
        return self.type


class Routers(models.Model):
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True, blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    sleeptime = models.SmallIntegerField(default=0)
    isActivated = models.BooleanField(default=False)
    devtype = models.ForeignKey(RoutersType, related_name='dev_type', on_delete=models.CASCADE, default='1')

    def __str__(self):
        return '{}:{}'.format(self.addr, self.port)

    class Meta:
        db_table = 'routers'

    def __str__(self):
        return self.addr + '/' + self.port

