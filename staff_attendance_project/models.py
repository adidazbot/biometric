# api/models.py

from django.db import models

class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)

class BiometricData(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    biometric_type = models.CharField(max_length=50)
    biometric_data = models.BinaryField()

class CheckInOut(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField(auto_now_add=True)
    checkout_time = models.DateTimeField(null=True, blank=True)
    is_checked_in = models.BooleanField(default=True)

