from django.db import models
from django.db.models import Sum
from datetime import datetime


class Customers(models.Model):
    CUST_STATUS = (
        (1, 'Zájemce'),
        (2, 'Čekající'),
        (3, 'Připojený'),
    )
    lastname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    status = models.SmallIntegerField(choices=CUST_STATUS)
    type = models.SmallIntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    ten = models.CharField(max_length=16)
    ssn = models.CharField(max_length=11)
    regon = models.CharField(max_length=255)
    rbe = models.CharField(max_length=255)
    icn = models.CharField(max_length=255)
    info = models.TextField()
    notes = models.TextField()
    serviceaddr = models.TextField()
    creationdate = models.IntegerField()
    moddate = models.IntegerField()
    creatorid = models.IntegerField()
    modid = models.IntegerField()
    deleted = models.BooleanField()
    message = models.TextField()
    pin = models.IntegerField()
    cutoffstop = models.IntegerField()
    consentdate = models.IntegerField()
    divisionid = models.IntegerField()
    paytime = models.IntegerField()
    paytype = models.SmallIntegerField(blank=True, null=True)
    deposit = models.DecimalField(max_digits=9, decimal_places=2)
    depositdate = models.IntegerField()
    sendinvoice = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'customers'

    def full_name(self):
        return '{} {}'.format(self.lastname, self.name)

    # def modify_event(self):
    #     if self.modid > 0:
    #         mod_user = Users.objects.get(id=self.modid).name
    #         return '{}, {}'.format(mod_user, datetime.utcfromtimestamp(self.moddate).strftime('%Y-%m-%d %H:%m:%S'))
    #     return ''

    # def balance(self):
    #     balance = Cash.objects.filter(customerid=self.id).aggregate(Sum('value'))
    #     return balance['value__sum']
    #
    # def create_event(self):
    #     if self.creatorid > 0:
    #         mod_user = Users.objects.get(id=self.creatorid).name
    #         return '{}, {}'.format(mod_user, datetime.utcfromtimestamp(self.creationdate).strftime('%Y-%m-%d %H:%m:%S'))
    #     return ''

    def depositdate_asstring(self):
        if self.depositdate:
            return datetime.utcfromtimestamp(self.depositdate).strftime('%Y-%m-%d')
        return ''

    def __str__(self):
        return 'CID: {} {} {}'.format(self.id, self.lastname, self.name)

