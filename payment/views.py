from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Credit, Payment
from .serializers import CreditSerializer, PaymentSerializer


class CreditViewSet(ModelViewSet):
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

    def list(self, request, *args, **kwargs):
        credits = Credit.objects.filter(status=1)
        lizings = Credit.objects.filter(status=2)
        credits_serializer = CreditSerializer(credits, many=True)
        lisings_serializer = CreditSerializer(lizings, many=True)
        data = {
            'credits': credits_serializer.data,
            'lisings': lisings_serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
