from django.db import models

# Create your models here.

class Events(models.Model):
    event_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)
    price=models.FloatField()
    limit=models.IntegerField()

class Hosts(models.Model):
    host_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    image=models.TextField()

class EventHosts(models.Model):
    event_host_id=models.AutoField(primary_key=True)
    event_id=models.ForeignKey(Events,on_delete=models.CASCADE)
    host_id=models.ForeignKey(Hosts,on_delete=models.CASCADE)

class Registration(models.Model):
    reg_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    phone=models.IntegerField(max_length=100)
    event_id=models.ForeignKey(Events,on_delete=models.CASCADE)
 