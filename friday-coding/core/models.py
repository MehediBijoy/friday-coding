from django.db import models
from django.utils import timezone

from users.models import User


class UserWallet(models.Model):
    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    balance = models.PositiveIntegerField(default=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.name


class Transaction(models.Model):
    status_choices = (
        ('init', 'Init'),
        ('successed', 'Successed'),
        ('failed', 'Failed')
    )
    sender = models.ForeignKey(
        User,
        related_name='sender',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    amount = models.PositiveIntegerField()
    recipient = models.ForeignKey(
        User,
        related_name='recipient',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    scheduled_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(choices=status_choices,
                              default='init',
                              max_length=255
                              )
    reason = models.CharField(max_length=255, null=True, blank=True)

    @property
    def transfer_now(self):
        if self.status == 'init' and (not self.scheduled_at or self.scheduled_at <= timezone.now()):
            return True
        else:
            return False

    def __str__(self) -> str:
        return self.sender.name
