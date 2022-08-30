from django.contrib import admin

from .models import UserWallet, Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['sender', 'amount', 'recipient',
                    'scheduled_at', 'status', 'reason']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class UserWalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance', 'updated_at']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserWallet, UserWalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
