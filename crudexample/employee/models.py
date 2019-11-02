from django.db import models
class Employee(models.Model):
    eid = models.CharField(max_length=20,default=None)
    ename = models.CharField(max_length=100,default=None)
    eemail = models.EmailField(default=None)
    econtact = models.CharField(max_length=15,default=None)
    class Meta:
        db_table = "employee"
