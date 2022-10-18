from django.db import models

class Location(models.Model) :
    locationname = models.CharField(max_length=30)
    def __str__(self):
        return  f"id={self.id}, locationname={self.locationname}"

class Department(models.Model) :
    deptid = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=30)
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    def __str__(self):
        return f"deptid={self.deptid}, deptname={self.deptname}, location={self.location}"

class Employee(models.Model) :
    name = models.CharField(max_length=8)
    addr = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return  f"name={self.name}, addr={self.addr}, department={self.department}"

