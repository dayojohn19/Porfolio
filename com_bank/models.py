from django.db import models
from app_mail.models import User

# Create your models here.
class Bank(models.Model):
    total_amount = models.IntegerField()
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    clients = models.ManyToManyField(User, default=None, blank=True, related_name="bank_clients")
    timestamp = models.DateTimeField(auto_now_add=True)

class schedule(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    amount = models.IntegerField()
    manager = models.CharField(max_length=94)
    clients = models.ManyToManyField(User, default=None, blank=True, related_name="schedule_clients")
    contact = models.CharField(max_length=94)

class Withdraw(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="withdraw_bank_id")
    user =  models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="withdraw_user")
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    approved = models.BooleanField(default=False)
    manager = models.CharField(blank=True, max_length=63)

class Deposit(models.Model):
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="deposit_bank_id")
    user = models.IntegerField()
    amount = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Transactions(models.Model):
    Transaction_type = models.CharField(max_length=94)
    bank_id = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="transaction_bank_id")
    user =  models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="transaction_user")
    timestamp = models.DateTimeField(auto_now_add=True)
