from django.db import models


class Nodes(models.Model):
    name = models.CharField(unique=True, max_length=32)
    ipaddr = models.PositiveIntegerField(unique=True)
    ipaddr_pub = models.PositiveIntegerField()
    passwd = models.CharField(max_length=32)
    ownerid = models.IntegerField()
    creationdate = models.IntegerField()
    moddate = models.IntegerField()
    creatorid = models.IntegerField()
    modid = models.IntegerField()
    netdev = models.IntegerField()
    linktype = models.IntegerField()
    port = models.SmallIntegerField()
    access = models.IntegerField()
    warning = models.IntegerField()
    chkmac = models.IntegerField()
    halfduplex = models.IntegerField()
    lastonline = models.IntegerField()
    info = models.TextField()
    location = models.TextField()
    nas = models.IntegerField()
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    linkspeed = models.IntegerField()
    kod_adm = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes'
