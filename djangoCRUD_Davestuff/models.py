from django.db import models


# create student table
# 1name
# 2email
# 3phone number

class Student(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.CharField(max_length=30, blank=False, null=False)
    phone = models.IntegerField(blank=False, null=False)


def __str__(self):
    return self.name
