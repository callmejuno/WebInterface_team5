from django.db import models

# Create your models here.

class DBTest(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField(null = True)

    def __str__(self):
        return self.name + ':' + str(self.age)

class Emp(models.Model):
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length = 10)
    job = models.CharField(max_length = 15)
    mgr = models.IntegerField()
    hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField(null = True)
    deptno = models.IntegerField()

    def __str__(self):
        return str(self.empno) + "," + self.ename + "," + str(self.hiredate)+\
            "," + str(self.sal) + "," + str(self.deptno)