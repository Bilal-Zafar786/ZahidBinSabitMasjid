from django.db import models


class StudentRegister(models.Model):
    Roll_Number = models.AutoField(primary_key=True)
    SName = models.CharField(max_length=100,default='')
    FatherName = models.CharField(max_length=100,default='')
    Address = models.CharField(max_length=500,default='')
    Cell_Number = models.IntegerField(max_length=20)
    Admission_Date = models.DateField()
    BForm = models.ImageField(upload_to='images/',default='')
    Promised_Fee = models.IntegerField(max_length=99999)

    class Meta:
        db_table = "std_registration"


from django.db import models

# Create your models here.
