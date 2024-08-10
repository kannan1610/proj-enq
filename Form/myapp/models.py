# models.py
from django.db import models
class Enquiry(models.Model):
    qualifications={
        "sslc":"SSLC",
        "hsc":"HSC",
        "diploma":"Diploma",
        "ug":"UG",
        "pg":"PG"
    }
    courses={
        6000:"Microsoft",
        8000:"Tally",
        10000:"Programming"
    }
    Schemes={
        10:"General",
        40:"Referal",
        80:"walking"
    }

    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=255)
    mobileno = models.CharField(max_length=20)
    whatsapp=models.BooleanField(default=False)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField()
    blood = models.CharField(max_length=10)
    qualification = models.CharField(max_length=50,choices=qualifications,default=None,null=True)
    stream=models.CharField(blank=True,max_length=50,null=False)
    course = models.CharField(max_length=20,choices=courses,default=None,null=True)
    scheme = models.CharField(max_length=10,choices=Schemes,default=None,null=True)
    parentmob = models.CharField(max_length=10)
    regno = models.CharField(max_length=20)
    joindate = models.DateField()


    def __str__(self):
        return self.username
