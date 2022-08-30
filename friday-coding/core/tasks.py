from celery import shared_task
from django.utils import timezone

from .models import Transaction
from .views import transferBalance


@shared_task(bind=True)
def first_task(self):
    objects = Transaction.objects.filter(
        status='init',
        scheduled_at__lt=timezone.now()
    )
    for object in objects:
        transferBalance(object)
