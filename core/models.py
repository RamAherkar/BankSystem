from django.db import models
from accounts.models import UserBankAccount, User

# Create your models here.
"""class Record(models.Model):
    account0 = models.ForeignKey(
        UserBankAccount,
        related_name='users',
        on_delete=models.CASCADE,
    )
    balance = User.balance
    username = User.username
    email = User.email
    account_type = UserBankAccount.account_type
    #account_no = User.account_no
    def __str__(self):
        return str(self.account.account_no)
            
"""