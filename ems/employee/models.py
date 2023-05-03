from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return self.name
    
    
    
    
class Role(models.Model):
    name = models.CharField(max_length=20, null=False)
    def __str__(self):
        return self.name



class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    salary = models.CharField(max_length=10)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    
    
    


