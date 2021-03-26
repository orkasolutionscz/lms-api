from django.db import models
import netaddr


class Nodes(models.Model):
    name = models.CharField(unique=True, max_length=32)
    ipaddr = models.PositiveIntegerField(unique=True)
    ipaddr_pub = models.PositiveIntegerField()
    passwd = models.CharField(max_length=32)
    # ownerid = models.IntegerField()
    owner = models.ForeignKey('api_customer.customers', related_name='owner', on_delete=models.CASCADE, db_column='ownerid')
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

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'nodes'


class Macs(models.Model):
    mac = models.CharField(max_length=17)
    nodeid = models.ForeignKey(Nodes, related_name='nodesmacs', on_delete=models.DO_NOTHING, db_column='nodeid')

    def __str__(self):
        return self.mac

    class Meta:
        managed = False
        db_table = 'macs'
        unique_together = (('mac', 'nodeid'),)


class BtIphistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.IntegerField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(db_column='CID', blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uzivatel = models.TextField(db_column='UZIVATEL', blank=True, null=True)  # Field name made lowercase.
    datum = models.DateTimeField(db_column='DATUM', blank=True, null=True)  # Field name made lowercase.

    def iptext(self):
        return str(netaddr.IPAddress(self.ip))

    def __str__(self):
        return self.iptext()

    class Meta:
        managed = False
        db_table = 'bt_iphistory'

