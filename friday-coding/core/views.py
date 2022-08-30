from django.db import transaction
from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import UserWallet, Transaction
from .serializers import TransactionHistorySerializer, TransterSerializer


@transaction.atomic
def transferBalance(object):
    try:
        sender = UserWallet.objects.filter(
            user=object.sender).select_for_update().first()
        recipient = UserWallet.objects.filter(
            user=object.recipient).select_for_update().first()

        if sender.balance - object.amount >= 0:
            sender.balance -= object.amount
            recipient.balance += object.amount

            sender.save()
            recipient.save()

            object.status = 'successed'
            object.save()
        else:
            raise ValueError('insaficint balance')
    except ValueError as e:
        object.status = 'failed'
        object.reason = f"{e}"
        object.save()


class TransferBalance(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        params = request.data
        if not len(params):
            raise ValidationError('Empty params')

        serializer = TransterSerializer(data=params, many=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        objects = serializer.save(sender=user)
        for object in objects:
            if object.transfer_now:
                transferBalance(object)

        return Response(data='request successfull')


class TransactionHistory(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        objects = Transaction.objects.filter(
            Q(sender=user) | Q(recipient=user)
        )
        return Response(data=TransactionHistorySerializer(objects, many=True).data)
