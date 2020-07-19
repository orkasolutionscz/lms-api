from django.db import models


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
