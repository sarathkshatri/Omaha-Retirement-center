from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    @property
    def is_orc_staff(self):
        if hasattr(self, 'orc_staff'):
            return True
        return False

    @property
    def is_resident(self):
        if hasattr(self, 'resident'):
            return True
        return False

    @property
    def is_maintenanceworker(self):
        if hasattr(self, 'maintenanceworker'):
            return True
        return False


marital_status = (
        ('--', "--"),
        ('Single', "Single"),
        ('Married', "Married"),
)

# Create your models here.
class Resident(models.Model):
    resident_id = models.AutoField(auto_created=True,primary_key=True,max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    resident_name = models.CharField(max_length=50)
    resident_occupation = models.CharField(max_length=50)
    resident_emailaddress=models.CharField(max_length=50)
    resident_marital_status=models.CharField(max_length=50,choices=marital_status, default='--')
    resident_familymember_count=models.IntegerField()
    resident_petdetails=models.CharField(max_length=50)
    resident_contactdetails=models.CharField(max_length=10)
    resident_startdate=models.DateField(default=timezone.now)
    resident_enddate=models.DateField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.resident_name)

    class Meta:
        verbose_name = 'Resident'
        verbose_name_plural = 'Resident'


class Orc_Staff(models.Model):
    orc_staff_id = models.AutoField(auto_created=True,primary_key=True,max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    orc_staff_name = models.CharField(max_length=50)
    orc_staff_emailaddress=models.CharField(max_length=50)
    orc_staff_address=models.CharField(max_length=50)
    orc_staff_yearsofexperience=models.IntegerField()
    orc_staff_contactdetails=models.CharField(max_length=10)
    orc_staff_position=models.CharField(max_length=50)
    orc_staff_startdate=models.DateTimeField(default=timezone.now)
    orc_staff_enddate=models.DateTimeField(default=timezone.now)
    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.orc_staff_name)

    class Meta:
        verbose_name = 'Orc_Staff'
        verbose_name_plural = 'Orc_Staff'


Floor=(
        ('--', '--'),
        ('Lower Ground', 'Lower Ground'),
        ('Ground', 'Ground'),
        ('First','First'),
        ('Second','Second'),
)


roomno=(
        ('--', '--'),
        ('Atlas101', 'Atlas101'),
        ('Atlas102', 'Atlas102'),
        ('Atlas103', 'Atlas103'),
        ('Atlas104', 'Atlas104'),
        ('Atlas201', 'Atlas201'),
        ('Atlas202', 'Atlas202'),
        ('Atlas203', 'Atlas203'),
        ('Atlas204', 'Atlas204'),
        ('Atlas301', 'Atlas301'),
        ('Atlas302', 'Atlas302'),
        ('Atlas303', 'Atlas303'),
        ('Atlas304', 'Atlas304'),
        ('Atlas401', 'Atlas401'),
        ('Atlas402', 'Atlas402'),
        ('Atlas403', 'Atlas403'),
        ('Atlas404', 'Atlas404'),
        ('Brook101', 'Brook101'),
        ('Brook102', 'Brook102'),
        ('Brook103', 'Brook103'),
        ('Brook104', 'Brook104'),
        ('Brook201', 'Brook201'),
        ('Brook202', 'Brook202'),
        ('Brook203', 'Brook203'),
        ('Brook204', 'Brook204'),
        ('Brook301', 'Brook301'),
        ('Brook302', 'Brook302'),
        ('Brook303', 'Brook303'),
        ('Brook304', 'Brook304'),
        ('Brook401', 'Brook401'),
        ('Brook402', 'Brook402'),
        ('Brook403', 'Brook403'),
        ('Brook404', 'Brook404'),
        ('AON101', 'AON101'),
        ('AON102', 'AON102'),
        ('AON103', 'AON103'),
        ('AON104', 'AON104'),
        ('AON201', 'AON201'),
        ('AON202', 'AON202'),
        ('AON203', 'AON203'),
        ('AON204', 'AON204'),
        ('AON301', 'AON301'),
        ('AON302', 'AON302'),
        ('AON303', 'AON303'),
        ('AON304', 'AON304'),
        ('AON401', 'AON401'),
        ('AON402', 'AON402'),
        ('AON403', 'AON403'),
        ('AON404', 'AON404'),
)

class Roomallotment(models.Model):
    allotment_id=models.AutoField(auto_created=True,primary_key=True,max_length=6)
    resident_name = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='residents1')
    property_number = models.CharField(max_length=50,choices=roomno,default='--')
    property_floor=models.CharField(max_length=50,choices=Floor,default='--')
    allotment_startdate=models.DateTimeField(default=timezone.now())
    allotment_enddate=models.DateTimeField(default=timezone.now())
    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.property_number)

    class Meta:
        verbose_name = 'Roomallotment'
        verbose_name_plural = 'Roomallotment'


priority_level = (
        ('--', '--'),
        ('Low', 'Low'),
        ('Moderate', 'Moderate'),
        ('High','High'),
)

workorder_cat=(
    ('--', '--'),
    ('Household Appliances', 'Household Appliances'),
    ('Furniture Repair', 'Furniture Repair'),
    ('Plumbling', 'Plumbling'),
    ('Pest Control','Pest Control'),
    ('Other Maintenance Work','Other Maintenance Work'),
)
class Workorder(models.Model):
    resident_name = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='resname')
    resident_id = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='resid')
    workorder_id = models.IntegerField(primary_key=True)
    workorder_Description= models.CharField(max_length=50)
    workorder_category=models.CharField(max_length=50,choices=workorder_cat, default='--')
    workorder_priority=models.CharField(max_length=50,choices=priority_level, default='--')
    property_number=models.ForeignKey(Roomallotment,on_delete=models.CASCADE,related_name='wo1')
    workorder_opendate=models.DateTimeField(default=timezone.now )
    workorder_duedate = models.DateTimeField(default=timezone.now)
    workorder_closedate=models.DateTimeField(default=timezone.now)
    is_open=models.BooleanField(default=True, blank=False, null=False)

    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.workorder_id)

    class Meta:
        verbose_name = 'Workorder'
        verbose_name_plural = 'Workorder'


class Equipment(models.Model):
    equipment_id = models.AutoField(auto_created=True,primary_key=True,max_length=6)
    equipment_serialnumber= models.CharField(max_length=10)
    equipment_name=models.CharField(max_length=10)
    equipment_description=models.CharField(max_length=50)
    is_available=models.BooleanField(default=True, blank=False, null=False)
    equipment_cost=models.IntegerField()
    equipment_purchasedate=models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.equipment_name)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'


class MaintenanceWorker(models.Model):
    worker_id = models.AutoField(auto_created=True,primary_key=True,max_length=6)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    maintenanceworker_name = models.CharField(max_length=50)
    worker_emailaddress=models.CharField(max_length=50)
    worker_address=models.CharField(max_length=50)
    worker_yearsofexperience=models.IntegerField()
    worker_contactdetails=models.CharField(max_length=10)
    worker_startdate=models.DateField(default=timezone.now)
    worker_enddate=models.DateField(default=timezone.now)
    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.maintenanceworker_name)

    class Meta:
        verbose_name = 'MaintenanceWorker'
        verbose_name_plural = 'MaintenanceWorker'


class MaintenanceWork(models.Model):
    residentid = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='residentid')
    maintenancework_id=models.AutoField(auto_created=True,primary_key=True,max_length=6)
    maintenancework_description=models.CharField(max_length=50)
    workorder_id = models.ForeignKey(Workorder, on_delete=models.CASCADE, related_name='mw1')
    worker_id = models.ForeignKey(MaintenanceWorker,on_delete=models.CASCADE, blank = True, null=True)
    maintenanceworker_name = models.ForeignKey(MaintenanceWorker, on_delete=models.CASCADE, related_name='mw2')
    equipment_name=models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='mw4')
    property_number=models.ForeignKey(Roomallotment,on_delete=models.CASCADE,related_name='mw3')
    maintenancework_cost=models.IntegerField()
    maintenancework_opendate=models.DateTimeField(default=timezone.now)
    maintenancework_duedate = models.DateTimeField(default=timezone.now)
    is_open=models.BooleanField(default=True, blank=False, null=False)
    maintenancework_closedate=models.DateTimeField(default=timezone.now)
    created_date = models.DateField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.maintenancework_id)

    class Meta:
        verbose_name = 'MaintenanceWork'
        verbose_name_plural = 'MaintenanceWork'
