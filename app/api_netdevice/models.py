from django.db import models


class Netdevices(models.Model):
    name = models.CharField(max_length=32)
    location = models.CharField(max_length=255)
    description = models.TextField()
    producer = models.CharField(max_length=64)
    model = models.CharField(max_length=32)
    serialnumber = models.CharField(max_length=32)
    ports = models.IntegerField()
    purchasetime = models.IntegerField()
    guaranteeperiod = models.PositiveIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=32)
    nastype = models.IntegerField()
    clients = models.IntegerField()
    secret = models.CharField(max_length=60)
    community = models.CharField(max_length=50)
    channelid = models.IntegerField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    hw_type = models.IntegerField()
    nms_group = models.IntegerField()
    wlan_freq = models.IntegerField()
    wlan_ch_width = models.IntegerField()
    wlan_antenna = models.IntegerField()
    wlan_polarization = models.IntegerField()
    wlan_cipher = models.CharField(max_length=100, blank=True, null=True)
    netssid = models.CharField(max_length=32)
    con_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'netdevices'
