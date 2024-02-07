from datetime import datetime, timedelta
from django.db import models

class User(models.Model):
    first_name          = models.CharField(max_length=50)
    last_name           = models.CharField(max_length=50)
    age                 = models.IntegerField()
    phone_number        = models.CharField(max_length=15, unique=True)
    monthly_salary      = models.FloatField()
    approved_limit      = models.FloatField()
    current_debt        = models.FloatField(default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def save(self, *args, **kwargs):
        self.approved_limit = int(36) * self.monthly_salary
        super(User, self).save(*args, **kwargs)

class Loan(models.Model):
    user                = models.ForeignKey(User, on_delete=models.CASCADE)
    loan_amount         = models.IntegerField(default=0)
    tenure              = models.IntegerField()
    interest_rate       = models.IntegerField(default=0)
    emi                 = models.FloatField(default=0)
    emi_paid            = models.IntegerField(default=0)
    start_date          = models.DateField()
    end_date            = models.DateField()

    def __str__(self):
        return self.id
