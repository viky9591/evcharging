from django.db import models

# Create your models here.

class user_table(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phoneno=models.BigIntegerField()
    
class user_request(models.Model): #for new user registration
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phoneno=models.BigIntegerField()
    request=models.CharField(max_length=15,default='pending')

    
class manager_table(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)    
    password=models.CharField(max_length=20)

class admin_table(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20)    
    password=models.CharField(max_length=20)

class stations_table(models.Model):
    id=models.AutoField(primary_key=True)
    location=models.CharField(max_length=20)

class slots_table(models.Model):
    id=models.AutoField(primary_key=True)
    slotno=models.IntegerField()
    station_id=models.ForeignKey(stations_table,on_delete=models.CASCADE)
    booking_status=models.CharField(max_length=15,default='avilable')
    chrging_status=models.CharField(max_length=15,default='inactive')  

class history_table(models.Model):
    id=models.AutoField(primary_key=True)
    dateTime=models.DateTimeField()
    username=models.CharField(max_length=20)
    location=models.CharField(max_length=15)
    slotno=models.IntegerField()
    bookingNo=models.IntegerField()             

        