from email.policy import default
from rest_framework import serializers
from .models import Transaction


class TransactionHistorySerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    recipient = serializers.StringRelatedField()

    class Meta:
        model = Transaction
        fields = '__all__'


class TransterSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Transaction
        fields = ['sender', 'amount', 'recipient', 'scheduled_at']

        extra_kargs = {
            'amount': {'required': True},
            'recipient': {'required': True},
            'scheduled_at': {'required': True}
        }

    def validate(self, validate_data):
        if not validate_data['recipient']:
            raise serializers.ValidationError('recipient required')

        if validate_data['recipient'] == self.context['request'].user:
            raise serializers.ValidationError(
                'sender and recipient must be different')

        if not validate_data['amount'] or validate_data['amount'] < 0:
            raise serializers.ValidationError(
                'non negative amont will be required')
        return validate_data
