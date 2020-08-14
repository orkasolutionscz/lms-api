from django.db import models


class RoutersType(models.Model):
    type = models.CharField(max_length=255)


class Routers(models.Model):
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True, blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    sleeptime = models.SmallIntegerField()
    isActivated = models.BooleanField(default=False)
    devtype = models.ForeignKey(RoutersType, on_delete=models.CASCADE, default='1')

    def __str__(self):
        return '{}:{}'.format(self.addr, self.port)
