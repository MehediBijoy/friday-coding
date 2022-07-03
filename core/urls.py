from django.urls import path

from .views import TransferBalance, TransactionHistory

urlpatterns = [
    path('transfer_balance/', TransferBalance.as_view()),
    path('transaction_history/', TransactionHistory.as_view()),
]
