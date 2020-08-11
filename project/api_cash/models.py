from django.db import models
from datetime import datetime


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

    def platba_datum(self):
        return datetime.utcfromtimestamp(self.time).strftime('%Y-%m-%d %H:%m:%S')

    class Meta:
        managed = False
        db_table = 'cash'



