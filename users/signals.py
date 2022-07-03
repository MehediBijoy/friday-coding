from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import User
from core.models import UserWallet


@receiver(post_save, sender=User)
def wallet_generate(sender, instance, created, **kwargs):
    if created:
        wallet = UserWallet.objects.create(
            user=instance
        )
        wallet.save()
