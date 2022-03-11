import uuid
from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=50)
    loan = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.account_name}"

class Rank(models.Model):
    Ranks = (
            (0, 'Basic'),
            (1, 'Silver'),
            (2, 'Gold'),
    )
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length = 20)
    rank = models.ForeignKey(Rank, choices=Rank.Ranks, on_delete=models.CASCADE, default=0, max_length=10)

class Ledger(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    text = models.CharField(max_length = 20)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_time = models.DateTimeField(auto_now_add=True, blank=True)
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
