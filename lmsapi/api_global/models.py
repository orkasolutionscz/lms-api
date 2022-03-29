from django.db import models


class GlobalVars(models.Model):
    varname = models.CharField(null=False, max_length=250)
    varsection = models.CharField(null=True, max_length=100, default=None)
    varvalue = models.CharField(null=False, max_length=250)

    class Meta:
        managed = False
        db_table = 'sysvars'
