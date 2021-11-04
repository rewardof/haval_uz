from rest_framework import serializers
from car.models import Car, PositionCategory
from .models import Credit, Payment
from car.serializers import PositionCategorySerializer


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'credit', 'order', 'percent', 'total', 'remain')


class CreditSerializer(serializers.ModelSerializer):
    models = serializers.SerializerMethodField()
    payments = PaymentSerializer(many=True, read_only=True)
    car = serializers.SlugRelatedField(queryset=Car.objects.all(), slug_field='title')

    class Meta:
        model = Credit
        fields = ('id', 'car', 'models', 'month', 'payments', 'status')

    def get_models(self, obj):
        position_category = PositionCategory.objects.get(pk=obj.model.pk)
        serializer = PositionCategorySerializer(position_category)
        return serializer.data
