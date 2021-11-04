from .models import Dealer
from .serializers import DealerSerializer
from rest_framework.viewsets import ModelViewSet


class DealerViewSet(ModelViewSet):
    queryset = Dealer.objects.all()
    serializer_class = DealerSerializer
