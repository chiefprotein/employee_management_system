from django.db import models

# Create your models here.


class emp(models.Model):
  empid=models.CharField(max_length=100,unique=True)
  empname=models.CharField(max_length=150,null=True)
  dateb=models.DateField(null=True)
  datej=models.DateField(null=True)
  department=models.CharField(max_length=150,null=True)
  age=models.IntegerField(null=True)
  address=models.CharField(max_length=300,null=True)
  salary=models.IntegerField(null=True)
  position=models.CharField(max_length=100,null=True)
  
  def __str__(self):
     return self.empname
  

  


class manager(models.Model):
  managerid=models.CharField(max_length=10,unique=True)
  managername=models.CharField(max_length=100)
  mdepartment=models.CharField(max_length=50)

  def __str__(self):
     return self.managerid

