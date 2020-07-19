# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aliasassignments(models.Model):
    aliasid = models.IntegerField()
    accountid = models.IntegerField()
    mail_forward = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'aliasassignments'
        unique_together = (('aliasid', 'accountid', 'mail_forward'),)


class Aliases(models.Model):
    login = models.CharField(max_length=255)
    domainid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aliases'
        unique_together = (('login', 'domainid'),)


class ApiRbbackupRouters(models.Model):
    addr = models.CharField(max_length=255)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    identity = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField()
    modify = models.DateTimeField(blank=True, null=True)
    lastbackup = models.DateTimeField(blank=True, null=True)
    sleeptime = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'api_rbbackup_routers'


class ApiSmsgwOutbox(models.Model):
    sms_source = models.CharField(max_length=50, blank=True, null=True)
    number = models.CharField(max_length=20)
    processed_date = models.DateTimeField(blank=True, null=True)
    insert_date = models.DateTimeField()
    text = models.CharField(max_length=160)
    processed = models.IntegerField()
    error = models.IntegerField()
    error_text = models.TextField(blank=True, null=True)
    not_before = models.TimeField()
    not_after = models.TimeField()

    class Meta:
        managed = False
        db_table = 'api_smsgw_outbox'


class Assignments(models.Model):
    tariffid = models.IntegerField()
    liabilityid = models.IntegerField()
    customerid = models.IntegerField()
    period = models.SmallIntegerField()
    at = models.IntegerField()
    datefrom = models.IntegerField()
    dateto = models.IntegerField()
    invoice = models.IntegerField()
    suspended = models.IntegerField()
    settlement = models.IntegerField()
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    paytype = models.SmallIntegerField(blank=True, null=True)
    numberplanid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assignments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class BtIphistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.IntegerField(db_column='IP', blank=True, null=True)  # Field name made lowercase.
    cid = models.IntegerField(db_column='CID', blank=True, null=True)  # Field name made lowercase.
    typ = models.CharField(db_column='TYP', max_length=1, blank=True, null=True)  # Field name made lowercase.
    uzivatel = models.TextField(db_column='UZIVATEL', blank=True, null=True)  # Field name made lowercase.
    datum = models.DateTimeField(db_column='DATUM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bt_iphistory'


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


class Cashimport(models.Model):
    date = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    customer = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    customerid = models.IntegerField()
    hash = models.CharField(max_length=50)
    closed = models.IntegerField()
    sourceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashimport'


class Cashreglog(models.Model):
    regid = models.IntegerField()
    userid = models.IntegerField()
    time = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    snapshot = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'cashreglog'
        unique_together = (('regid', 'time'),)


class Cashregs(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    in_numberplanid = models.IntegerField()
    out_numberplanid = models.IntegerField()
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cashregs'


class Cashrights(models.Model):
    userid = models.IntegerField()
    regid = models.IntegerField()
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cashrights'
        unique_together = (('userid', 'regid'),)


class Cashsources(models.Model):
    name = models.CharField(unique=True, max_length=32)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cashsources'


class Comments(models.Model):
    domain_id = models.IntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=10)
    modified_at = models.IntegerField()
    account = models.CharField(max_length=40)
    comment = models.TextField()

    class Meta:
        managed = False
        db_table = 'comments'


class Countries(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'countries'


class Cryptokeys(models.Model):
    domain_id = models.IntegerField()
    flags = models.IntegerField()
    active = models.IntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cryptokeys'


class Customerassignments(models.Model):
    customergroupid = models.IntegerField()
    customerid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customerassignments'
        unique_together = (('customergroupid', 'customerid'),)


class Customercontacts(models.Model):
    customerid = models.IntegerField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'customercontacts'


class Customergroups(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'customergroups'


class Customers(models.Model):
    lastname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    status = models.SmallIntegerField()
    type = models.SmallIntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    countryid = models.IntegerField()
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
    deleted = models.IntegerField()
    message = models.TextField()
    pin = models.IntegerField()
    cutoffstop = models.IntegerField()
    consentdate = models.IntegerField()
    divisionid = models.IntegerField()
    paytime = models.IntegerField()
    paytype = models.SmallIntegerField(blank=True, null=True)
    deposit = models.DecimalField(max_digits=9, decimal_places=2)
    depositdate = models.IntegerField()
    sendinvoice = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'customers'


class Daemonconfig(models.Model):
    instanceid = models.IntegerField()
    var = models.CharField(max_length=64)
    value = models.TextField()
    description = models.TextField()
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'daemonconfig'
        unique_together = (('instanceid', 'var'),)


class Daemoninstances(models.Model):
    name = models.CharField(max_length=255)
    hostid = models.IntegerField()
    module = models.CharField(max_length=255)
    crontab = models.CharField(max_length=255)
    priority = models.IntegerField()
    description = models.TextField()
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'daemoninstances'


class Dbinfo(models.Model):
    keytype = models.CharField(primary_key=True, max_length=255)
    keyvalue = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'dbinfo'


class Debitnotecontents(models.Model):
    docid = models.IntegerField()
    itemid = models.SmallIntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'debitnotecontents'
        unique_together = (('docid', 'itemid'),)


class Divisions(models.Model):
    shortname = models.CharField(unique=True, max_length=255)
    name = models.TextField()
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    countryid = models.IntegerField()
    ten = models.CharField(max_length=16)
    regon = models.CharField(max_length=255)
    account = models.CharField(max_length=48)
    inv_header = models.TextField()
    inv_footer = models.TextField()
    inv_author = models.TextField()
    inv_cplace = models.TextField()
    description = models.TextField()
    status = models.IntegerField()
    inv_paytime = models.IntegerField(blank=True, null=True)
    inv_paytype = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'divisions'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Docrights(models.Model):
    userid = models.IntegerField()
    doctype = models.IntegerField()
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docrights'
        unique_together = (('userid', 'doctype'),)


class Documentcontents(models.Model):
    docid = models.IntegerField(unique=True)
    title = models.TextField()
    fromdate = models.IntegerField()
    todate = models.IntegerField()
    filename = models.CharField(max_length=255)
    contenttype = models.CharField(max_length=255)
    md5sum = models.CharField(max_length=32)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'documentcontents'


class Documents(models.Model):
    type = models.IntegerField()
    number = models.IntegerField()
    numberplanid = models.IntegerField()
    extnumber = models.CharField(max_length=255)
    cdate = models.IntegerField()
    customerid = models.IntegerField()
    userid = models.IntegerField()
    divisionid = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    countryid = models.IntegerField()
    ten = models.CharField(max_length=16)
    ssn = models.CharField(max_length=11)
    paytime = models.IntegerField()
    closed = models.IntegerField()
    reference = models.IntegerField()
    reason = models.CharField(max_length=255)
    infotext = models.CharField(max_length=255)
    paytype = models.SmallIntegerField(blank=True, null=True)
    taxdate = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'documents'


class Domainmetadata(models.Model):
    domain_id = models.IntegerField()
    kind = models.CharField(max_length=32, blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domainmetadata'


class Domains(models.Model):
    ownerid = models.IntegerField()
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    master = models.CharField(max_length=128, blank=True, null=True)
    last_check = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=6)
    notified_serial = models.IntegerField(blank=True, null=True)
    account = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'domains'


class Eventassignments(models.Model):
    eventid = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'eventassignments'
        unique_together = (('eventid', 'userid'),)


class Events(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    note = models.TextField()
    date = models.IntegerField()
    begintime = models.SmallIntegerField()
    endtime = models.SmallIntegerField()
    userid = models.IntegerField()
    customerid = models.IntegerField()
    private = models.IntegerField()
    closed = models.IntegerField()
    ticketid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'events'


class EwxChannels(models.Model):
    name = models.CharField(unique=True, max_length=32)
    upceil = models.IntegerField()
    downceil = models.IntegerField()
    upceil_n = models.IntegerField(blank=True, null=True)
    downceil_n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ewx_channels'


class EwxPtConfig(models.Model):
    nodeid = models.IntegerField(unique=True)
    name = models.CharField(max_length=32)
    mac = models.CharField(max_length=20)
    ipaddr = models.PositiveIntegerField()
    passwd = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'ewx_pt_config'


class EwxStmChannels(models.Model):
    cid = models.IntegerField(unique=True)
    upceil = models.IntegerField()
    downceil = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ewx_stm_channels'


class EwxStmNodes(models.Model):
    nodeid = models.IntegerField(unique=True)
    mac = models.CharField(max_length=20)
    ipaddr = models.PositiveIntegerField()
    channelid = models.IntegerField()
    uprate = models.IntegerField()
    upceil = models.IntegerField()
    downrate = models.IntegerField()
    downceil = models.IntegerField()
    halfduplex = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ewx_stm_nodes'


class Excludedgroups(models.Model):
    customergroupid = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'excludedgroups'
        unique_together = (('userid', 'customergroupid'),)


class Ftpquotatallies(models.Model):
    name = models.CharField(max_length=30)
    quota_type = models.CharField(max_length=5)
    bytes_in_used = models.FloatField()
    bytes_out_used = models.FloatField()
    bytes_xfer_used = models.FloatField()
    files_in_used = models.PositiveIntegerField()
    files_out_used = models.PositiveIntegerField()
    files_xfer_used = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ftpquotatallies'


class Groups(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=30)
    status = models.CharField(max_length=1, blank=True, null=True)
    group_password = models.CharField(max_length=64)
    gid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'


class Hosts(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()
    lastreload = models.IntegerField()
    reload = models.IntegerField()
    lastreload_uid = models.IntegerField()
    seq = models.IntegerField()
    lastfail = models.IntegerField()
    lastsucc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hosts'


class Hwtypes(models.Model):
    vendor_id = models.IntegerField()
    name = models.CharField(unique=True, max_length=100)
    hw_profile = models.CharField(max_length=50)
    ports = models.IntegerField()
    shortname = models.CharField(max_length=10)
    def_wlan_freq = models.IntegerField(blank=True, null=True)
    def_wlan_ch_width = models.IntegerField(blank=True, null=True)
    def_wlan_antenna = models.IntegerField(blank=True, null=True)
    def_wlan_polarization = models.IntegerField(blank=True, null=True)
    oidmacvlanadr = models.CharField(max_length=100)
    oidmacvlandescr = models.CharField(max_length=100)
    oidmacvlanvlanid = models.CharField(max_length=100)
    oidmacvlanstatus = models.CharField(max_length=100)
    oidvlanid = models.CharField(max_length=100)
    oidvlandescr = models.CharField(max_length=100)
    oidvlanstatus = models.CharField(max_length=100)
    snmp_portconfig = models.TextField()

    class Meta:
        managed = False
        db_table = 'hwtypes'


class Imessengers(models.Model):
    customerid = models.IntegerField()
    uid = models.CharField(max_length=32)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'imessengers'


class Invoicecontents(models.Model):
    docid = models.IntegerField()
    itemid = models.SmallIntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2)
    taxid = models.IntegerField()
    prodid = models.CharField(max_length=255)
    content = models.CharField(max_length=16)
    count = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    tariffid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoicecontents'


class Liabilities(models.Model):
    value = models.DecimalField(max_digits=9, decimal_places=2)
    name = models.TextField()
    taxid = models.IntegerField()
    prodid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'liabilities'


class Macs(models.Model):
    mac = models.CharField(max_length=17)
    nodeid = models.ForeignKey('Nodes', models.DO_NOTHING, db_column='nodeid')

    class Meta:
        managed = False
        db_table = 'macs'
        unique_together = (('mac', 'nodeid'),)


class Managementurls(models.Model):
    netdevid = models.ForeignKey('Netdevices', models.DO_NOTHING, db_column='netdevid')
    url = models.TextField()
    comment = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'managementurls'


class Messageitems(models.Model):
    messageid = models.IntegerField()
    customerid = models.IntegerField()
    destination = models.CharField(max_length=255)
    lastdate = models.IntegerField()
    status = models.SmallIntegerField()
    error = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messageitems'


class Messages(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    cdate = models.IntegerField()
    type = models.SmallIntegerField()
    userid = models.IntegerField()
    sender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messages'


class Nastypes(models.Model):
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'nastypes'


class Netcontypes(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=15)
    popis = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'netcontypes'


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


class Netlinks(models.Model):
    src = models.IntegerField()
    dst = models.IntegerField()
    type = models.IntegerField()
    srcport = models.SmallIntegerField()
    dstport = models.SmallIntegerField()
    speed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'netlinks'
        unique_together = (('src', 'dst'),)


class Networks(models.Model):
    name = models.CharField(unique=True, max_length=255)
    address = models.PositiveIntegerField(unique=True)
    mask = models.CharField(max_length=16)
    gateway = models.CharField(max_length=16)
    interface = models.CharField(max_length=32)
    vlanid = models.IntegerField(blank=True, null=True)
    dns = models.CharField(max_length=16)
    dns2 = models.CharField(max_length=16)
    domain = models.CharField(max_length=64)
    wins = models.CharField(max_length=16)
    dhcpstart = models.CharField(max_length=16)
    dhcpend = models.CharField(max_length=16)
    disabled = models.IntegerField()
    notes = models.TextField()
    dhcprelayip = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'networks'


class Nmsgroups(models.Model):
    name = models.CharField(max_length=150)
    notes = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmsgroups'


class Nmshosts(models.Model):
    host_id = models.IntegerField(primary_key=True)
    host_name = models.CharField(max_length=32)
    host_ip = models.TextField()
    host_groupname = models.TextField()
    host_desc = models.TextField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nmshosts'


class Nodeassignments(models.Model):
    nodeid = models.ForeignKey('Nodes', models.DO_NOTHING, db_column='nodeid')
    assignmentid = models.ForeignKey(Assignments, models.DO_NOTHING, db_column='assignmentid')

    class Meta:
        managed = False
        db_table = 'nodeassignments'
        unique_together = (('nodeid', 'assignmentid'),)


class Nodegroupassignments(models.Model):
    nodegroupid = models.IntegerField()
    nodeid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nodegroupassignments'
        unique_together = (('nodeid', 'nodegroupid'),)


class Nodegroups(models.Model):
    name = models.CharField(unique=True, max_length=255)
    prio = models.IntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'nodegroups'


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
    con_type = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes'


class NodesConType(models.Model):
    id = models.IntegerField(primary_key=True)
    typ = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'nodes_con_type'


class Numberplanassignments(models.Model):
    planid = models.IntegerField()
    divisionid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'numberplanassignments'
        unique_together = (('planid', 'divisionid'),)


class Numberplans(models.Model):
    template = models.CharField(max_length=255)
    period = models.SmallIntegerField()
    doctype = models.IntegerField()
    isdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'numberplans'


class Passwd(models.Model):
    ownerid = models.IntegerField()
    login = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    lastlogin = models.IntegerField()
    uid = models.IntegerField()
    home = models.CharField(max_length=255)
    type = models.SmallIntegerField()
    expdate = models.IntegerField()
    domainid = models.IntegerField()
    quota_sh = models.IntegerField()
    quota_mail = models.IntegerField()
    quota_www = models.IntegerField()
    quota_ftp = models.IntegerField()
    quota_sql = models.IntegerField()
    realname = models.CharField(max_length=255)
    createtime = models.IntegerField()
    mail_forward = models.CharField(max_length=255)
    mail_bcc = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'passwd'
        unique_together = (('login', 'domainid'),)


class Payments(models.Model):
    name = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=9, decimal_places=2)
    creditor = models.CharField(max_length=255)
    period = models.SmallIntegerField()
    at = models.SmallIntegerField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'payments'


class Receiptcontents(models.Model):
    docid = models.IntegerField()
    itemid = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    regid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'receiptcontents'


class Records(models.Model):
    domain = models.ForeignKey(Domains, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    change_date = models.IntegerField(blank=True, null=True)
    lms_export = models.IntegerField()
    disabled = models.IntegerField()
    ordername = models.CharField(max_length=255, blank=True, null=True)
    auth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'records'


class RecordsTmp(models.Model):
    domain_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=6, blank=True, null=True)
    content = models.CharField(max_length=255, blank=True, null=True)
    ttl = models.IntegerField(blank=True, null=True)
    prio = models.IntegerField(blank=True, null=True)
    change_date = models.IntegerField(blank=True, null=True)
    lms_export = models.IntegerField()
    disabled = models.IntegerField()
    ordername = models.CharField(max_length=255, blank=True, null=True)
    auth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'records_tmp'


class Rtattachments(models.Model):
    messageid = models.ForeignKey('Rtmessages', models.DO_NOTHING, db_column='messageid')
    filename = models.CharField(max_length=255)
    contenttype = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'rtattachments'


class Rtmessages(models.Model):
    ticketid = models.ForeignKey('Rttickets', models.DO_NOTHING, db_column='ticketid')
    userid = models.IntegerField()
    customerid = models.IntegerField()
    mailfrom = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    messageid = models.CharField(max_length=255)
    inreplyto = models.IntegerField()
    replyto = models.TextField()
    headers = models.TextField()
    body = models.TextField()
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rtmessages'


class Rtnotes(models.Model):
    ticketid = models.ForeignKey('Rttickets', models.DO_NOTHING, db_column='ticketid')
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    body = models.TextField()
    createtime = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rtnotes'


class Rtqueues(models.Model):
    name = models.CharField(unique=True, max_length=255)
    email = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'rtqueues'


class Rtrights(models.Model):
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='userid')
    queueid = models.ForeignKey(Rtqueues, models.DO_NOTHING, db_column='queueid')
    rights = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rtrights'
        unique_together = (('userid', 'queueid'),)


class Rttickets(models.Model):
    queueid = models.ForeignKey(Rtqueues, models.DO_NOTHING, db_column='queueid')
    requestor = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    state = models.IntegerField()
    cause = models.IntegerField()
    owner = models.IntegerField()
    customerid = models.IntegerField()
    creatorid = models.IntegerField()
    createtime = models.IntegerField()
    resolvetime = models.IntegerField()
    resolvedby = models.IntegerField()
    priority = models.IntegerField()
    deadline = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'rttickets'


class Ruian(models.Model):
    kod_adm = models.IntegerField(primary_key=True)
    kod_obce = models.IntegerField(blank=True, null=True)
    nazev_obce = models.CharField(max_length=255, blank=True, null=True)
    nazev_momp = models.CharField(max_length=255, blank=True, null=True)
    nazev_moc = models.CharField(max_length=255, blank=True, null=True)
    kod_casti_obce = models.IntegerField(blank=True, null=True)
    nazev_casti_obce = models.CharField(max_length=255, blank=True, null=True)
    nazev_ulice = models.CharField(max_length=255, blank=True, null=True)
    typ_so = models.CharField(max_length=255, blank=True, null=True)
    cislo_domovni = models.IntegerField(blank=True, null=True)
    cislo_orientacni = models.IntegerField(blank=True, null=True)
    znak_cisla_orientacniho = models.CharField(max_length=255, blank=True, null=True)
    psc = models.IntegerField(blank=True, null=True)
    souradnice_y = models.CharField(max_length=255, blank=True, null=True)
    souradnice_x = models.CharField(max_length=255, blank=True, null=True)
    plati_od = models.CharField(max_length=255, blank=True, null=True)
    kod_momc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ruian'


class Sessions(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    ctime = models.IntegerField()
    mtime = models.IntegerField()
    atime = models.IntegerField()
    vdata = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'sessions'


class States(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'states'


class Stats(models.Model):
    nodeid = models.IntegerField()
    dt = models.IntegerField()
    upload = models.BigIntegerField(blank=True, null=True)
    download = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stats'
        unique_together = (('nodeid', 'dt'),)


class Supermasters(models.Model):
    ip = models.CharField(max_length=25)
    nameserver = models.CharField(max_length=255)
    account = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supermasters'


class Tariffs(models.Model):
    name = models.CharField(unique=True, max_length=255)
    type = models.IntegerField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    taxid = models.IntegerField()
    prodid = models.CharField(max_length=255)
    uprate = models.IntegerField()
    upceil = models.IntegerField()
    downrate = models.IntegerField()
    downceil = models.IntegerField()
    climit = models.IntegerField()
    plimit = models.IntegerField()
    dlimit = models.IntegerField()
    domain_limit = models.IntegerField(blank=True, null=True)
    alias_limit = models.IntegerField(blank=True, null=True)
    sh_limit = models.IntegerField(blank=True, null=True)
    www_limit = models.IntegerField(blank=True, null=True)
    mail_limit = models.IntegerField(blank=True, null=True)
    ftp_limit = models.IntegerField(blank=True, null=True)
    sql_limit = models.IntegerField(blank=True, null=True)
    quota_sh_limit = models.IntegerField(blank=True, null=True)
    quota_www_limit = models.IntegerField(blank=True, null=True)
    quota_mail_limit = models.IntegerField(blank=True, null=True)
    quota_ftp_limit = models.IntegerField(blank=True, null=True)
    quota_sql_limit = models.IntegerField(blank=True, null=True)
    description = models.TextField()
    uprate_n = models.IntegerField(blank=True, null=True)
    upceil_n = models.IntegerField(blank=True, null=True)
    downrate_n = models.IntegerField(blank=True, null=True)
    downceil_n = models.IntegerField(blank=True, null=True)
    climit_n = models.IntegerField(blank=True, null=True)
    plimit_n = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tariffs'


class Taxes(models.Model):
    value = models.DecimalField(max_digits=4, decimal_places=2)
    taxed = models.IntegerField()
    label = models.CharField(max_length=16)
    validfrom = models.IntegerField()
    validto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'taxes'


class Testtbl(models.Model):
    one = models.AutoField(primary_key=True)
    two = models.IntegerField()
    three = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'testtbl'


class Tsigkeys(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    algorithm = models.CharField(max_length=50, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tsigkeys'
        unique_together = (('name', 'algorithm'),)


class Uiconfig(models.Model):
    section = models.CharField(max_length=64)
    var = models.CharField(max_length=64)
    value = models.TextField()
    description = models.TextField()
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'uiconfig'
        unique_together = (('section', 'var'),)


class UpCustomers(models.Model):
    customerid = models.IntegerField()
    lastlogindate = models.IntegerField()
    lastloginip = models.CharField(max_length=16)
    failedlogindate = models.IntegerField()
    failedloginip = models.CharField(max_length=16)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'up_customers'


class UpHelp(models.Model):
    reference = models.IntegerField()
    title = models.CharField(max_length=128)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'up_help'


class UpInfoChanges(models.Model):
    customerid = models.IntegerField()
    fieldname = models.CharField(max_length=255)
    fieldvalue = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'up_info_changes'


class UpRights(models.Model):
    module = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True, null=True)
    setdefault = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'up_rights'


class UpRightsAssignments(models.Model):
    customerid = models.IntegerField()
    rightid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'up_rights_assignments'
        unique_together = (('customerid', 'rightid'),)


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


class Vendors(models.Model):
    name = models.CharField(unique=True, max_length=100)
    hide = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vendors'


class Voipaccounts(models.Model):
    ownerid = models.IntegerField()
    login = models.CharField(max_length=255)
    passwd = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    creationdate = models.IntegerField()
    moddate = models.IntegerField()
    creatorid = models.IntegerField()
    modid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'voipaccounts'


class Wlanantennas(models.Model):
    name = models.CharField(max_length=250)
    gain = models.IntegerField()
    vert_angle = models.IntegerField()
    horz_angle = models.IntegerField()
    polarization = models.CharField(max_length=50, blank=True, null=True)
    freq_range = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=250, blank=True, null=True)
    hide = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'wlanantennas'


class Wlanfreqs(models.Model):
    name = models.CharField(max_length=50)
    freq = models.IntegerField()
    channel = models.IntegerField()
    note = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wlanfreqs'


class Zipcodes(models.Model):
    zip = models.CharField(unique=True, max_length=10)
    stateid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'zipcodes'
