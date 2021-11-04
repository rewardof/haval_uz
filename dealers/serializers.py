from rest_framework import serializers
from .models import Dealer


class DealerForPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('id', 'title', 'position')


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'
