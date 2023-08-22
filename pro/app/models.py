from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=30)
    mobile = models.IntegerField()
    salary = models.IntegerField()
    bonus = models.IntegerField()
    profile_image = models.ImageField(upload_to='media/', null=True, default=None)
    dob = models.DateField()
    address = models.TextField(max_length=500, default=True)
    cv = models.FileField(upload_to='resume/', null=True, default=None)
    # category = models.Choices()

    class Meta:
        ordering = ['-id']
