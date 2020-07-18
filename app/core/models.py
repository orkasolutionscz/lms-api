from django.db import models


class Cash(models.Model):
    time = models.IntegerField()
    type = models.SmallIntegerField()
    userid = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    taxid = models.IntegerField()
    customerid = models.IntegerField()
    comment = models.TextField()
    docid = models.IntegerField()
    itemid = models.SmallIntegerField()
    importid = models.IntegerField(blank=True, null=True)
    sourceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cash'


class UserGroup(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user_group'


class Users(models.Model):
    login = models.CharField(unique=True, max_length=32)
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    rights = models.CharField(max_length=64)
    hosts = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    lastlogindate = models.IntegerField()
    lastloginip = models.CharField(max_length=16)
    failedlogindate = models.IntegerField()
    failedloginip = models.CharField(max_length=16)
    deleted = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
