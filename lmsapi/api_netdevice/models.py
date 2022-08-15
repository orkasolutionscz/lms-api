from django.db import models


class Netcontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=15)
    popis = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'netcontypes'


class Wlanfranges(models.Model):
    name = models.CharField(max_length=50)
    hide = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'wlanfranges'


class Wlanfreqs(models.Model):
    ref_ad = models.ForeignKey(Wlanfranges, on_delete=models.DO_NOTHING, db_column='ref_ad')
    name = models.CharField(max_length=50)
    freq = models.IntegerField()
    channel = models.IntegerField()
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wlanfreqs'


class Hwtypes(models.Model):
    vendor_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)
    hw_profile = models.CharField(max_length=50)
    ports = models.IntegerField()
    shortname = models.CharField(max_length=10)
    def_wlan_freq = models.ForeignKey(Wlanfranges, on_delete=models.DO_NOTHING, db_column='def_wlan_freq')
    def_wlan_ch_width = models.IntegerField(blank=True, null=True)
    def_wlan_antenna = models.IntegerField(blank=True, null=True)
    def_wlan_polarization = models.IntegerField(blank=True, null=True)
    snmp_portconfig = models.TextField()

    class Meta:
        managed = False
        db_table = 'hwtypes'


class Nmsgroups(models.Model):
    name = models.CharField(max_length=150)
    notes = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmsgroups'


class Wlanmodes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    apmode = models.CharField(max_length=32)
    popis = models.CharField(max_length=255, blank=True, null=True)
    nas_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wlanmodes'


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
    hw_type = models.ForeignKey(Hwtypes, on_delete=models.DO_NOTHING, db_column='hw_type')
    nms_group = models.ForeignKey(Nmsgroups, on_delete=models.DO_NOTHING, db_column='nms_group')
    wlan_freq = models.IntegerField()
    wlan_ch_width = models.IntegerField()
    wlan_antenna = models.IntegerField()
    wlan_polarization = models.IntegerField()
    wlan_cipher = models.CharField(max_length=100, blank=True, null=True)
    netssid = models.CharField(max_length=32)
    con_type = models.ForeignKey(Netcontypes, on_delete=models.DO_NOTHING, db_column='con_type')
    wlan_mode = models.ForeignKey(Wlanmodes, on_delete=models.DO_NOTHING, db_column='wlan_mode')

    class Meta:
        managed = False
        db_table = 'netdevices'
