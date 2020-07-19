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



